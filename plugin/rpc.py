from PyPresence import Presence
from PyPresence import exceptions
import time, sys, json


client_id = '765583106610298881' 
try:
    RPC = Presence(client_id)  # Initialize the client class
    RPC.connect() # Start the handshake loop
except ConnectionResetError:
    sys.exit()
except exceptions.InvalidID:
    sys.exit()


editing_file_name = sys.argv[1]         # file name
workspace = sys.argv[2]                 # workspace (cwd)
show_workspace = sys.argv[3]            # show workpace in the rpc?

try:
    ext = editing_file_name.split(".")[1]
except:
    ext = ""

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
    #'capnp': "Cap'n' Proto",
    'java': 'java',
    #'ex': 'Elixir',
    'md': 'md',
    'ts': 'typescript',
    'go': 'golang',
    'kt': 'kotlin',
    'kts': 'kotlin',
    #'cr': 'Crystal',
    'rb': 'ruby',
    'clj': 'clojure',
    'hs': 'haskell',
    'json': 'json',
    'vue': 'vue',
    #'groovy': 'Groovy',
    'swift': 'swift',
    'lua': 'lua',
    'jl': 'julia',
    'dart': 'dart',
    #'pp': 'Pascal',
}

if(editing_file_name == "Idle"):
    st = "Idle"
    de = ""
elif show_workspace == "true":
    st = "Editing {}".format(editing_file_name)
    de = "Workspace: {}".format(workspace)
else:
    st = "Editing {}".format(editing_file_name)
    de = ""

# Start time
e = time.time()

# keep updating rpc
while True:
    if ext in thumbnails:
        try:
            if de == "":
                RPC.update(state=st, large_image=thumbnails[ext], start=e)
            else:
                RPC.update(state=st, details=de, large_image=thumbnails[ext], start=e)
        except ConnectionResetError:
            RPC.close()
            sys.exit()
        except exceptions.InvalidID:
            RPC.close()
            sys.exit()
    else:
        try:
            RPC.update(state=st, large_image="vim", start=e)
        except ConnectionResetError:
            RPC.close()
            sys.exit()
        except exceptions.InvalidID:
            RPC.close()
            sys.exit()
    time.sleep(15)

