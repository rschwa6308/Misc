# Russell Schwartz's custom git bash command prompt config
# found at C:/Users/Russell/.config/git/git-prompt.sh


PS1='\[\033]0;$TITLEPREFIX:\W\007\]'	# set window title
# PS1="$PS1"'\[\033[32m\]'                # change to green
# PS1="$PS1"'\u@\h '                      # user@host<space>
PS1="$PS1"'\[\033[35m\]'                # change to purple
PS1="$PS1"'[\s] '                       # show [bash]
PS1="$PS1"'\[\033[33m\]'                # change to yellow
PS1="$PS1"'\w'                          # current working directory


if test -z "$WINELOADERNOEXEC"
then
	GIT_EXEC_PATH="$(git --exec-path 2>/dev/null)"
	COMPLETION_PATH="${GIT_EXEC_PATH%/libexec/git-core}"
	COMPLETION_PATH="${COMPLETION_PATH%/lib/git-core}"
	COMPLETION_PATH="$COMPLETION_PATH/share/git/completion"
	if test -f "$COMPLETION_PATH/git-prompt.sh"
	then
		. "$COMPLETION_PATH/git-completion.bash"
		. "$COMPLETION_PATH/git-prompt.sh"
		PS1="$PS1"'\[\033[36m\]'    # change color to cyan
		PS1="$PS1"'`__git_ps1`'     # bash function (display current branch name)
	fi
fi


PS1="$PS1"'\n'              # new line
PS1="$PS1"'\[\033[32m\]'	# change to green
PS1="$PS1"'❯ '              # custom prompt character (default is '$ ')
# PS1="$PS1"'🡲 '             # custom prompt character (default is '$ ')
PS1="$PS1"'\[\033[0m\]'     # change color


# print a newline immediately before $PS1
# (cute little hack to skip the very first prompt)
PROMPT_COMMAND="export PROMPT_COMMAND=echo"
