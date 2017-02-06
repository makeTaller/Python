let SessionLoad = 1 if &cp | set nocp | endif let s:cpo_save=&cpo set cpo&vim map! <S-Insert> * nnoremap   nnoremap <NL> <NL> nnoremap   nnoremap   vmap  "*d nnoremap   za nmap gx <Plug>NetrwBrowseX nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0) vmap <C-Del> "*d vmap <S-Del> "*d vmap <C-Insert> "*y vmap <S-Insert> "-d"*P nmap <S-Insert> "*P let &cpo=s:cpo_save unlet s:cpo_save set background=dark set encoding=utf-8 set fileencodings=ucs-bom,utf-8,default,latin1 set guifont=Consolas:h14:cANSI set helplang=En set splitbelow set splitright set window=38 let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0 let v:this_session=expand("<sfile>:p") silent only cd ~\Desktop if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == '' let s:wipebuf = bufnr('%') endif set shortmess=aoO badd +23 \Users\david\Documents\GitHub\Python\Session.vim silent! argdel * set splitbelow splitright wincmd t set winheight=1 winwidth=1 argglobal enew setlocal keymap= setlocal noarabic setlocal noautoindent setlocal balloonexpr= setlocal nobinary setlocal bufhidden= setlocal buflisted setlocal buftype= setlocal nocindent setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e setlocal cinoptions= setlocal cinwords=if,else,while,do,for,switch setlocal colorcolumn= setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:- setlocal commentstring=/*%s*/ setlocal complete=.,w,b,u,t,i setlocal concealcursor= setlocal conceallevel=0 setlocal completefunc= setlocal nocopyindent setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != ''
setlocal filetype=
endif
setlocal foldcolumn=0
setlocal nofoldenable
setlocal foldexpr=0
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=8
setlocal noshortname
setlocal nosmartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != ''
setlocal syntax=
endif
setlocal tabstop=8
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
