
python3 << en

from pypresence import Presence # The simple rich presence client in pypresence
import time, sys, vim
import threading

client_id = "765583106610298881"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client


RPC.connect() # Start the handshake loop

def start():
    fn = vim.eval("expand('%:t')")

    if(fn == ""):
        s = "Idling"
    else:
        s = "Editing " + fn

    e = int(time.time())

    RPC.update(state=s, large_image="vim", start=e) # Updates our presence


en

" Start RPC on startup and update on Change file
autocmd  BufReadPost *  :python3 start()
autocmd  VimEnter *  :python3 start()

