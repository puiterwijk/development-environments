#!/bin/bash -xe
# First pull down the latest versions of base envs
#docker pull fedora:latest

# Now build all envs
function buildenv() {
    if [ "$1" != "refresh.sh" ];
    then
        (
            cd $1
            docker build -t puiterwijk.org/development/$1:latest .
        )
    fi
}

function refresh_base(){
    for env in base*
    do
        buildenv $env
    done
}

function refresh_all(){
    for env in *
    do
        buildenv $env
    done
}

function refresh_all_async(){
    for env in *
    do
        buildenv $env &
    done
}
