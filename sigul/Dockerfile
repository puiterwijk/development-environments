FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y autoconf automake make gcc fedora-packager python-nss \
                   python-sqlalchemy rpm-sign ostree-devel python-pexpect \
                   psmisc gnupg

RUN dnf downgrade -y https://kojipkgs.fedoraproject.org//packages/python-nss/0.16.0/1.fc23/x86_64/python-nss-0.16.0-1.fc23.x86_64.rpm
