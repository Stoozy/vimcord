from PyPresence import Presence
import time, sys, json


client_id = '765583106610298881'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

fn = sys.argv[1]

try:
    ext = fn.split(".")[1]
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

if(fn == "Idle"):
    st = "Idle"
else:
    st = "Editing {}".format(fn)

# Start time
e = time.time()
if ext in thumbnails:
    RPC.update(state=st, large_image="vim", small_image=thumbnails[ext], start=e)
else:
    RPC.update(state=st, large_image="vim", start=e)

while True:
    if ext in thumbnails:
        RPC.update(state=st, large_image="vim", small_image=thumbnails[ext], start=e)
    else:
        RPC.update(state=st, large_image="vim", start=e)
    time.sleep(500)


