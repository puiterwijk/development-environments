FROM fedora:23
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && dnf update -y \
    && usermod -aG wheel docker

RUN dnf install -y vim

ENTRYPOINT ["/bin/bash"]
