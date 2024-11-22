### Root PS1 Colors ###
export PS1="\[$(tput bold)\]\[\033[38;5;196m\]\u\[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;15m\]@\[$(tput sgr0)\]\[\033[38;5;2m\]\h\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]\[\033[38;5;172m\]\W\[$(tput sgr0)\]\[\033[38;5;15m\]\n\\$ \[$(tput sgr0)\]"
### Root PS1 Colors ###
export HISTCONTROL=ignoredups
source /etc/bash/bash_completion.sh
alias update='apk update && apk upgrade'
export HISTTIMEFORMAT="%d/%m/%y %T "
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
# enable bash completion in interactive shells
export HISTTIMEFORMAT="%d/%m/%y %T "
export TERM=xterm-256color
export COLOR_PROMPT=yes
export LANG=C.UTF-8
export PIP_NO_CACHE_DIR=off
export PIP_DISABLE_PIP_VERSION_CHECK=on
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
export COLUMNS=80

# Clean __pycache__ folder
pyclean () {
    find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}
