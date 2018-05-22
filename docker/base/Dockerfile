FROM registry.fedoraproject.org/fedora:latest
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/userhome/project"]
# Stupid glibc/rpmdb/... bug
RUN dnf update -y glibc || true

RUN useradd docker -d /userhome -M \
    && usermod -aG wheel docker \
    && chown -R docker:docker /userhome \
    && dnf update -y \
    && dnf install -y vim sudo \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/docker

WORKDIR /userhome/project
ENTRYPOINT ["/bin/bash"]
