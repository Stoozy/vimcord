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
        if(fn == ""):
            fn = "Idle" 
        global s, pid
        s = subprocess.Popen("python3 {}/rpc.py  {}".format(adir, fn), shell=True)
        pid = s.pid

def kill():
    try:
        s.terminate()
    except NameError:
        print("")        
    try:
        os.system("kill {}".format(pid)) 
    except:
        print("Discord rpc not killed")
        
en

autocmd VimEnter * :python3 start()
autocmd BufNewFile * :execute 'python3 kill()' | :python3 start()
autocmd BufReadPre * :execute 'python3 kill()' | :python3 start()
autocmd VimLeavePre * :execute 'python3 kill()'
