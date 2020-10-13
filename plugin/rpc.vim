
python3 << en
from pypresence import Presence # The simple rich presence client in pypresence
import time, sys, vim

client_id = "765583106610298881"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client


RPC.connect() # Start the handshake loop
def start():
    n = vim.eval("expand('%')")
    e = int(time.time())
    s = "Editing "+n

    RPC.update(state=s, large_image="vim", start=e) # Updates our presence

#while True:  # The presence will stay on as long as the program is running
    #time.sleep(15) # Can only update rich presence every 15 seconds

en
" :python3 start(echo expand('%:t'))
" :python3 vim.eval("expand('')")
:python3 start()

