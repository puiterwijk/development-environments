FROM centos:7
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker

RUN yum install -y vim

ENTRYPOINT ["/bin/bash"]
