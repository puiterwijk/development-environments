#!/bin/bash -x
# First pull down the latest versions of base envs
docker pull fedora:latest

# Now build all envs
for env in base nodejs;
do
    (
        cd $env
        docker build -t puiterwijk.org/development/$env:latest .
    )
done
