FROM registry.fedoraproject.org/fedora:rawhide
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y sl

ENTRYPOINT ["/bin/sl", "-Fal"]
