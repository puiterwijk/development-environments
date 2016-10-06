FROM registry.access.redhat.com/rhel6/rhel:latest
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd -u 1000 docker -d /project -M \
    && usermod -aG wheel docker

RUN yum install -y vim \
    https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

ENTRYPOINT ["/bin/bash"]
