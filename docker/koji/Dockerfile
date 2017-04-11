FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y krb5-workstation koji

ENTRYPOINT ["/usr/bin/koji"]
USER docker
