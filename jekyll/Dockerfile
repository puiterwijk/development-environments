FROM centos:7
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker

RUN yum install -y ruby-devel make gcc-c++ libffi-devel redhat-rpm-config \
                   zlib-devel patch git
RUN gem install github-pages

ENTRYPOINT ["/bin/bash"]
