FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y krb5-workstation

CMD ["/usr/bin/klist"]
USER docker
