import vim
import os
import sys
import time
from dataclasses import dataclass


 # This is needed for imports
sys.path.append(vim.eval('g:vimcord_root_dir') + "/python3/vimcord")
ASYNC = int(vim.eval('vimcord_async'))

if ASYNC:
    import asyncio
    from pypresence import AioPresence, DiscordNotFound
else:
    from pypresence import Presence, DiscordNotFound
from thumbnails import thumbnailsDictionary


@dataclass
class FileMetaData:
    name: str
    extension: str
    workspace: str

    def __init__(self, vim):
        self.name =  vim.eval("expand('%:t')")
        self.extension =  vim.eval("expand('%:e')")
        self.workspace = vim.eval("expand('%:p:h:t')")


class Vimcord:
    def __init__(self) -> None:

        if ASYNC:
            self.rpc  = AioPresence('765583106610298881')
        else:
            self.rpc  = Presence('765583106610298881')
        self.connected = False
        self.start_time = int(time.time())

        self.vim = 'nvim' if int(vim.eval("g:vimcord_nvim")) == 1 else 'vim'

    def connect(self):
        if ASYNC:
            asyncio.create_task(self.rpc.connect())
            self.connected = True
        else:
            self.rpc.connect()
            self.connected = True

    def update(self):
        if not self.connected:
            print("Vimcord not connected");

        fmd = FileMetaData(vim)
        state = "Editing {}".format(fmd.name) if fmd.name != '' else "Idling"
        details = "Workspace {}".format(fmd.workspace)


        try:
            if ASYNC:
                asyncio.create_task(self.rpc.update(state=state, 
                    details=details, 
                    large_image=thumbnailsDictionary[fmd.extension] if fmd.extension in thumbnailsDictionary else thumbnailsDictionary[self.vim], 
                    start=self.start_time))
            else:
                self.rpc.update(state=state, 
                    details=details, 
                    large_image=thumbnailsDictionary[fmd.extension] if fmd.extension in thumbnailsDictionary else thumbnailsDictionary[self.vim],
                    start=self.start_time)
        except DiscordNotFound:
            print("Vimcord: Discord not open.")
        except:
            print("Vimcord: Error occured.")

    def kill(self):
        self.rpc.close()
        self.connected = False
