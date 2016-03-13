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

for env in base*
do
    buildenv $env
done

for env in *
do
    buildenv $env
done
