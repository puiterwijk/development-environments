#!/bin/bash -x
# First pull down the latest versions of base envs
docker pull fedora:latest

# Now build all envs
for env in base base-el7 base-el6 nodejs ipsilon ipsilon-el7 ipsilon-el6 python packaging;
do
    (
        cd $env
        docker build -t puiterwijk.org/development/$env:latest .
    )
done
