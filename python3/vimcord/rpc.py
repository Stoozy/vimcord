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
        self.workspace = os.path.basename(os.path.normpath(vim.eval("g:vimcord_workspace")))


class Vimcord:
    def __init__(self) -> None:

        if ASYNC:
            try:
                self.rpc  = AioPresence('765583106610298881')
            except DiscordNotFound:
                print("Discord not open")
            except:
                # print("Vimcord crashed")
                pass
        else:
            try:
                self.rpc  = Presence('765583106610298881')
            except DiscordNotFound:
                print("Discord not open")
            except:
                # print("Vimcord crashed")
                pass

        self.connected = False
        self.start_time = int(time.time())

        self.vim = 'nvim' if int(vim.eval("g:vimcord_nvim")) == 1 else 'vim'

    def connect(self):
        if ASYNC:
            try:
                asyncio.create_task(self.rpc.connect())
                self.connected = True
            except DiscordNotFound:
                print("Discord not open")
                self.connected = False
            except:
                self.connected = False
                # print("Vimcord crashed")


        else:
            try:
                self.rpc.connect()
                self.connected = True
            except DiscordNotFound:
                print("Discord not open")
            except:
                # print("Vimcord crashed")
                pass



    def update(self):
        if not self.connected:
            # print("Vimcord not connected");
            return

        fmd = FileMetaData(vim)
        state = "Editing {}".format(fmd.name) if fmd.name != '' else "Idling"
        details = "Workspace {}".format(fmd.workspace)


        if ASYNC:
            try:
                asyncio.create_task(self.rpc.update(state=state, 
                    details=details, 
                    large_image=thumbnailsDictionary[fmd.extension] if fmd.extension in thumbnailsDictionary else thumbnailsDictionary[self.vim], 
                    start=self.start_time))
            except DiscordNotFound:
                # print("Discord closed. Vimcord Exiting...")
                self.connected = False
            except:
                pass

        else:
            try:
                self.rpc.update(state=state, 
                    details=details, 
                    large_image=thumbnailsDictionary[fmd.extension] if fmd.extension in thumbnailsDictionary else thumbnailsDictionary[self.vim],
                    start=self.start_time)
            except DiscordNotFound:
                print("Discord not open")
            except:
                pass
                # print("Vimcord crashed")

    def kill(self):
        try:
            self.rpc.close()
        except:
            pass
        self.connected = False
