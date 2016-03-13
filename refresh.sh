#!/bin/bash -xe
# First pull down the latest versions of base envs
for fedver in rawhide 22 23;
do
    docker pull fedora:$fedver
    docker tag --force fedora:$fedver puiterwijk.org/development/base/fedora:$fedver
done
for centver in 6 7;
do
    docker pull centos:$centver
    docker tag --force centos:$centver puiterwijk.org/development/base/centos:$centver
done

docker run --privileged --rm=true --name "refresh" -v /var/run:/var/run:rw -v `pwd`:/mnt:r --entrypoint=/bin/bash -t fedora:rawhide -c "dnf install -y python3-yaml python3-docker-py && python3 /mnt/build.py"
