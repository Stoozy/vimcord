if !has("python3")
    echo "vim has to be compiled with +python to run vimcord"
    finish
endif

let g:vimcord_root_dir = expand('<sfile>:p:h:h')

if has("nvim")
  let g:vimcord_nvim = 1
  let g:vimcord_async = 1
  python3 import asyncio

  python3 from vimcord.rpc import Vimcord
  python3 vimcord = Vimcord()

  " COMMANDS

  command! VimcordConnect python3 vimcord.connect()
  command! VimcordUpdate python3 vimcord.update()
  command! VimcordDisconnect python3 vimcord.kill()

else
  let g:vimcord_nvim = 0
  let g:vimcord_async = 0

  python3 from vimcord.rpc import Vimcord
  python3 vimcord = Vimcord()

  " FUNCTIONS

  function! VimcordConnect()
    python3 vimcord.connect()
  endfunction


  function! VimcordUpdate()
    python3 vimcord.update()
  endfunction

  function! VimcordDisconnect()
    python3 vimcord.kill()
  endfunction

  " COMMANDS

  command! -nargs=0 VimcordConnect call VimcordConnect()
  command! -nargs=0 VimcordUpdate call VimcordUpdate()
  command! -nargs=0 VimcordDisconnect call VimcordDisconnect()

endif

autocmd VimEnter    * : execute 'VimcordConnect' | VimcordUpdate
autocmd BufNewFile  * : VimcordUpdate
autocmd InsertEnter * : VimcordUpdate
autocmd BufReadPre  * : VimcordUpdate
autocmd VimLeavePre * : VimcordDisconnect
