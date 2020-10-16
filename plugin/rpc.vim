if !has("python3")
    echo "vim has to be compiled with +python to run this"
    finish
endif

let g:vimrpcdir = expand('<sfile>:p:h')

python3 << en
import os, subprocess,vim
import psutil    

import subprocess
# check if discord is open
processes = subprocess.Popen('ps aux | grep Discord', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).communicate()[0]

global d
if(len(processes) != 0):
    d = True

def start():
    if not d:
        fn = vim.eval("expand('%:t')")
        adir = vim.eval("vimrpcdir")
        if(fn == ""):
            fn = "Idle" 
        global s
        s = subprocess.Popen("python3 {}/rpc.py  {}".format(adir, fn), shell=True)

def kill():
    try:
        s.terminate()
    except NameError:
        print("")
en

autocmd VimEnter * :python3 start()
autocmd BufReadPre * :execute 'python3 kill()' | :python3 start()
autocmd VimLeave * :python3 kill()
