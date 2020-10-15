from PyPresence import Presence
import time, sys 

client_id = '765583106610298881'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

fn = sys.argv[1]
if(fn == "Idle"):
    st = "Idle"
else:
    st = "Editing {}".format(fn)

# Start time
e = time.time()
RPC.update(state=st, large_image="vim", start=e)


while True:
    RPC.update(state=st, large_image="vim", start=e)
    time.sleep(500)


