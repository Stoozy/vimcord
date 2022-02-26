if !has("python3")
    echo "vim has to be compiled with +python to run vimcord"
    finish
endif

let g:vimrpcdir = expand('<sfile>:p:h')

python3 << en

# Some global
thumbnails = {
    'vim':'vim',
    'html': 'html',
    'css': 'css',
    'js': 'javascript',
    'php': 'php',
    'scss': 'sass',
    'py': 'python',
    'rs': 'rust',
    'c': 'c',
    'h': 'c',
    'cpp': 'cpp',
    'hpp': 'cpp',
    'cxx': 'cpp',
    'cc': 'cpp',
    'cs': 'c_sharp',
    'java': 'java',
    'md': 'md',
    'ts': 'typescript',
    'go': 'golang',
    'kt': 'kotlin',
    'kts': 'kotlin',
    'rb': 'ruby',
    'clj': 'clojure',
    'hs': 'haskell',
    'json': 'json',
    'vue': 'vue',
    'swift': 'swift',
    'lua': 'lua',
    'jl': 'julia',
    'dart': 'dart',
}

# Initialize RPC connection
import os, subprocess, vim, sys, time
import psutil

plugin_path = vim.eval("g:vimrpcdir")
python_module_path = os.path.abspath('%s' % (plugin_path))

sys.path.append(python_module_path)

from pypresence import Presence

client_id = '765583106610298881'
RPC = Presence(client_id)

is_connected = True

try: 
    RPC.connect()
except:
    is_connected = False

# Start time
e = time.time()

def kill():
    if is_connected:
        RPC.close()
    else:
        return

def update():
    if not is_connected:
        print("couldn't connect")
        return

    file_name =  vim.eval("expand('%:t')")
    file_extension =   vim.eval("expand('%:e')")
    workspace_dir = vim.eval("expand('%:p:h:t')")

    _state = "Editing {}".format(file_name) 
    _details = "Workspace {}".format(workspace_dir) 

    if file_extension in thumbnails:
        try:
            RPC.update(state=_state, details=_details, large_image = thumbnails[file_extension],   start = e)
        except:
            RPC.close()
    else:
        try:
            RPC.update(state=_state, details=_details, large_image="vim", start=e)
        except:
            RPC.close()
en

autocmd VimEnter    * :python3 update()
autocmd BufNewFile  * :python3 update()
autocmd InsertEnter * :python3 update()
autocmd BufReadPre  * :python3 update()
autocmd VimLeavePre * :python3 kill()

