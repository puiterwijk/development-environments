FROM registry.fedoraproject.org/fedora:latest
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
# Stupid glibc/rpmdb/... bug
RUN dnf update -y glibc || true

RUN useradd docker -d /project -M \
    && usermod -aG wheel docker \
    && chown docker:docker /project \
    && dnf update -y \
    && dnf install -y vim sudo \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/docker

WORKDIR /project
ENTRYPOINT ["/bin/bash"]
