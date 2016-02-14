FROM centos:6
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd -u 1000 docker -d /project -M \
    && usermod -aG wheel docker

RUN yum install -y vim epel-release

ENTRYPOINT ["/bin/bash"]
