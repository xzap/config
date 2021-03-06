#####################################################################################################
#shopt -s histappend
#setxkbmap -option terminate:ctrl_alt_bksp
PS1="$(if [[ ${EUID} == 0 ]]; then echo '\[\033[01;31m\]'; else echo '\[\033[01;32m\]\u@'; fi)\[\033[01;34m\] \w \$([[ \$? != 0 ]] && echo \"\[\033[01;31m\]:(\[\033[01;34m\] \")\$\[\033[00m\] "

PATH=$PATH:/home/xzap/bin


source /usr/share/doc/pkgfile/command-not-found.bash

complete -cf sudo
complete -cf man

#别名 #####################################################################################################
# modified commands
alias pacman='sudo pacman'
alias diff='colordiff'              # requires colordiff package
alias grep='grep --color=auto'
alias more='less'
alias df='df -h'
alias du='du -c -h'
alias mkdir='mkdir -p -v'
alias nano='nano -w'
alias ping='ping -c 5'
alias ..='cd ..'

# new commands
alias da='date "+%A, %B %d, %Y [%T]"'
alias du1='du --max-depth=1'
alias hist='history | grep $1'      # requires an argument
alias openports='netstat --all --numeric --programs --inet --inet6'
alias pg='ps -Af | grep $1'         # requires an argument (note: /usr/bin/pg is installed by the util-linux package; maybe a different alias name should be used)

# privileged access
if [ $UID -ne 0 ]; then
    alias sudo='sudo '
    alias scat='sudo cat'
    alias svim='sudo vim'
    alias root='sudo su'
    alias reboot='sudo reboot'
    alias halt='sudo halt'
    alias update='sudo pacman -Su'
    alias netcfg='sudo netcfg2'
fi

# ls
alias ls='ls -hF --color=auto'
alias lr='ls -R'                    # recursive ls
alias ll='ls -l'
alias la='ll -A'
alias lx='ll -BX'                   # sort by extension
alias lz='ll -rS'                   # sort by size
alias lt='ll -rt'                   # sort by date
alias lm='la | more'

# safety features
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -I'                    # 'rm -i' prompts for every file
alias ln='ln -i'
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'

# pacman aliases (if applicable, replace 'pacman' with 'yaourt'/'pacaur'/whatever)
#alias pac="pacman -S"      # default action     - install one or more packages
#alias pacu="pacman -Syu"   # '[u]pdate'         - upgrade all packages to their newest version
#alias pacs="pacman -Ss"    # '[s]earch'         - search for a package using one or more keywords
#alias paci="pacman -Si"    # '[i]nfo'           - show information about a package
#alias pacr="pacman -R"     # '[r]emove'         - uninstall one or more packages
#alias pacl="pacman -Sl"    # '[l]ist'           - list all packages of a repository
#alias pacll="pacman -Qqm"  # '[l]ist [l]ocal'   - list all packages which were locally installed (e.g. AUR packages)
#alias paclo="pacman -Qdt"  # '[l]ist [o]rphans' - list all packages which are orphaned
#alias paco="pacman -Qo"    # '[o]wner'          - determine which package owns a given file
#alias pacf="pacman -Ql"    # '[f]iles'          - list all files installed by a given package
#alias pacc="pacman -Sc"    # '[c]lean cache'    - delete all not currently installed package files
#alias pacm="makepkg -fci"  # '[m]ake'           - make package from PKGBUILD file in current directory
#alias pacman="sudo pacman-color"
#函数 #####################################################################################################

#[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx

