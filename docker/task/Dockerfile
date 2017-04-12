FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y task
COPY taskrc /project/.taskrc
VOLUME ["/tasks"]

ENTRYPOINT ["/usr/bin/task"]
USER docker
