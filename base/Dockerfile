FROM fedora:latest
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker

RUN dnf install -y vim

ENTRYPOINT ["/bin/bash"]
