" 使用 murphy 调色板
syntax enable
"set background=dark
colorscheme murphy
"color solarized
" 设置用于GUI图形用户界面的字体列表。
set guifont=WenQuanYi\ Micro\ Hei\ Mono\ 12
set nocompatible
" 设定文件浏览器目录为当前目录
set bsdir=buffer
set autochdir
set number

" 自动补全命令时候使用菜单式匹配列表
set wildmenu
" 允许退格键删除
set backspace=2
" 启用鼠标
set mouse=a
" 文件类型
filetype on
filetype plugin on
filetype indent on
" 设置编码自动识别, 中文引号显示
"set fileencodings=utf-8,cp936,big5,euc-jp,euc-kr,latin1,ucs-bom
set fileencodings=utf-8,gbk
set ambiwidth=double

" 移动长行
nnoremap <Down> gj
nnoremap <Up> gk

" 高亮
syntax on
" 设置高亮搜索
set hlsearch
" 输入字符串就显示匹配点
set incsearch
" 输入的命令显示出来，看的清楚些。
set showcmd

" 打开当前目录文件列表
map <F3> :e .<CR>

" Taglist
let Tlist_File_Fold_Auto_Close=1
set updatetime=1000
map <F4> :Tlist<CR>
syntax on
let tlist_txt_settings = 'txt;c:content;f:figures;t:tables'
au BufRead,BufNewFile *.txt setlocal ft=txt

" 按 F8 智能补全
inoremap <F8> <C-x><C-o>
" vim 自动补全 Python 代码
" 来自http://vim.sourceforge.net/scripts/script.php?script_id=850
autocmd FileType python set complete+=k/home/xzap/.vim/bundle/pydiction
" autocmd BufNewFile *.py 0r ~/.vim/template/simple.py


"Format the statusline
"Nice statusbar
set laststatus=2
set statusline=
set statusline+=%2*%-3.3n%0*\ " buffer number
set statusline+=%f\ " file name
set statusline+=%h%1*%m%r%w%0* " flag
set statusline+=[
if v:version >= 600
set statusline+=%{strlen(&ft)?&ft:'none'}, " filetype
set statusline+=%{&encoding}, " encoding
endif
set statusline+=%{&fileformat}] " file format
if filereadable(expand("$VIM/vimfiles/plugin/vimbuddy.vim"))
set statusline+=\ %{VimBuddy()} " vim buddy
endif
set statusline+=%= " right align
"set statusline+=%2*0x%-8B\ " current char
set statusline+=0x%-8B\ " current char
set statusline+=%-14.(%l,%c%V%)\ %<%P " offset


"20110506======================================
au BufEnter *.txt setlocal ft=txt
autocmd BufEnter *.txt set guifont=Vera\ Sans\ YuanTi\ Mono\ 16
autocmd BufEnter *.txt set linespace=6  
autocmd BufEnter *.txt set ambiwidth=double
autocmd BufEnter *.txt set wrap 
autocmd BufEnter *.txt set guioptions-=m 
autocmd BufEnter *.txt set guioptions-=T
autocmd BufEnter *.txt set laststatus=1

let Tlist_Ctags_Cmd="/usr/bin/ctags"   "设定ctags程序的位置。也许你需要修改下目录/usr/local/bin/ctags
"let Tlist_Auto_Open=1         "自动打开taglist窗口
let Tlist_Show_One_File = 1      "只显示当前文件的tag
let Tlist_Exit_OnlyWindow = 1      "如果taglist是最后一个窗口，则退出vim
":let Tlist_Use_Right_Window = 1      "在右侧窗口中显示taglist窗口
let Tlist_WinWidth = 18      "设定taglist窗口宽度
let Tlist_Inc_Winwidth = 0     "设定编辑窗口宽度


 "Set mapleade
  let mapleader = ","

  "Fast reloading of the .vimrc
 map <silent> <leader>ss :source ~/.vimrc<cr>
 "Fast editing of .vimrc
  map <silent> <leader>ee :e ~/.vimrc<cr>
 "When .vimrc is edited, reload it
 autocmd! bufwritepost .vimrc source ~/.vimrc
 """"""""""""""""""""""""""""""
" winManager setting
""""""""""""""""""""""""""""""
let g:winManagerWindowLayout = "BufExplorer,FileExplorer|TagList"
let g:winManagerWidth = 30
let g:defaultExplorer = 0
nmap <C-W><C-F> :FirstExplorerWindow<cr>
nmap <C-W><C-B> :BottomExplorerWindow<cr>
nmap <silent> <leader>wm :WMToggle<cr>
map <F3> :WMToggle<CR>
"“””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””
"” F7 NERDTree
"“””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””
map <F7> :NERDTreeToggle<CR>
imap <F7> <ESC>:NERDTreeToggle<CR>

""""""""""""""""""""""""""""""
" BufExplorer
""""""""""""""""""""""""""""""
let g:bufExplorerDefaultHelp=0
let g:bufExplorerShowRelativePath=1 "
let g:bufExplorerSortBy='mru'
let g:bufExplorerSplitRight=0
let g:bufExplorerSplitVertSize = 30 "
let g:bufExplorerUseCurrentWindow=1 "
autocmd BufWinEnter \[Buf\ List\] set nonumber

nnoremap <F5> :GundoToggle<CR>

set undodir=~/.vim/undodir
set undofile
set undolevels =1000 "maximum number of changes that can be undone
set undoreload =10000 "maximum number lines to save for undo on a buffer


:au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal g'\"" | endif


"pydiction 1.2 python auto complete
let g:pydiction_location = '/home/xzap/.vim/bundle/pydiction/complete-dict' 
"defalut g:pydiction_menu_height == 15
"let g:pydiction_menu_height = 20

"set filetype=python
au BufNewFile,BufRead *.py,*.pyw setf python
set autoindent " same level indent
set smartindent " next level indent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4

let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1

filetype plugin on

"set ofu=syntaxcomplete#Complete
"autocmd FileType python set omnifunc=pythoncomplete#Complete
"autocmd FileType python runtime! autoload/pythoncomplete.vim
