FROM fedora:rawhide
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker \
    && chown docker:docker /project \
    && dnf install -y vim sudo \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/docker

ENTRYPOINT ["/bin/bash"]
