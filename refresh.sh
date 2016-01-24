#!/bin/bash -x
for env in base nodejs;
do
    (
        cd $env
        docker build -t puiterwijk.org/development/$env:latest .
    )
done
