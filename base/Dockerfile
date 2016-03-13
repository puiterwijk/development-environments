FROM puiterwijk.org/base/fedora:rawhide
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker \
    && chown docker:docker /project \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/docker \
    && dnf install -y vim sudo

ENTRYPOINT ["/bin/bash"]
