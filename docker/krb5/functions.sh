#!/bin/bash
function dkcmd() {
    cmd=$1
    shift
    sudo docker run --rm=true -it --user docker --security-opt seccomp=$HOME/Documents/Development/Environments/docker/krb5/policy.json --cap-drop=ALL --security-opt="label=level:s0-s0:c0.c1023" --entrypoint=/bin/$cmd puiterwijk.org/development/krb5 $@
}

alias dklist="dkcmd klist"
alias dkinit="dkcmd kinit"
alias dkdestroy="dkcmd kdestroy"
alias dkpasswd="dkcmd kpasswd"
alias dkswitch="dkcmd kswitch"
alias dktutil="dkcmd ktutil"
alias dkvno="dkcmd kvno"
