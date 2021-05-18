if !has("python3")
    "vim has to be compiled with +python to run this"
    finish
endif

let g:vimrpcdir = expand('<sfile>:p:h')

python3 << en
import os, subprocess,vim, sys
import psutil

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def start():
    # check if discord is open
    if(checkIfProcessRunning("Discord")):
        fn = vim.eval("expand('%:t')")
        adir = vim.eval("vimrpcdir")
        cwd = vim.eval("getcwd()").split("/")[-1]

        # check if global flag exists
        if vim.eval("exists('g:vimcord_show_workspace')") == '1':
            if vim.eval("g:vimcord_show_workspace") == "true":
                show_workspace = "true"
            else:
                show_workspace = "false"
        else:
            # true by default
            show_workspace = "true"

        if(fn == ""):
            fn = "Idle" 

        global s, pid
        s = subprocess.Popen("python3 {}/rpc.py {} {} {}".format(adir, fn, cwd, show_workspace), shell=True)
        pid = s.pid

def kill():
    try:
        s.terminate()
    except NameError:
        print("")        
    try:
        os.system("kill {}".format(pid)) 
    except:
        pass
en

autocmd VimEnter    * :execute 'python3 kill()'     | :python3 start()
autocmd BufNewFile  * :execute 'python3 kill()'     | :python3 start()
autocmd BufReadPre  * :execute 'python3 kill()'     | :python3 start()
autocmd VimLeavePre * :execute 'python3 kill()'

