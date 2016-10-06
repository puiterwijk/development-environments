FROM registry.access.redhat.com/rhel7/rhel:latest
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker

RUN yum install -y vim \
    https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

ENTRYPOINT ["/bin/bash"]
