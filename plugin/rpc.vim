if !has("python3")
    echo "vim has to be compiled with +python to run this"
    finish
endif

python3 << en
import os, subprocess,vim

def start():
    fn = vim.eval("expand('%:t')")
    if(fn == ""):
        fn = "Idle" 
    global s
    s = subprocess.Popen("python3 ./rpc.py {}".format(fn), shell=True)
def kill():
    s.terminate()
en


autocmd VimEnter * :python3 start()
autocmd BufReadPre * :execute 'python3 kill()' | :python3 start()
autocmd VimLeave * :python3 kill()

