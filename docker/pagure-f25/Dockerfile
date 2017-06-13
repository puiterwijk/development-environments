FROM registry.fedoraproject.org/fedora:25
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

VOLUME ["/project"]
RUN useradd docker -d /project -M \
    && usermod -aG wheel docker \
    && chown docker:docker /project \
    && dnf update -y \
    && dnf install -y vim sudo \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/docker

WORKDIR /project
ENTRYPOINT ["/bin/bash"]

RUN dnf install -y python2-devel python-setuptools python-nose py-bcrypt python-alembic \
                   python-arrow python-binaryornot python-bleach python-blinker \
                   python-chardet python-cryptography python-docutils python-flask \
                   python-flask-wtf python-flask-multistatic python-markdown python-psutil \
                   python-pygit2 python-pygments python-fedora python-openid python-openid-cla \
                   python-openid-teams python-straight-plugin python-wtforms python-munch \
                   python-enum34 python-redis python-sqlalchemy systemd gitolite3 python-trollius \
                   python-trollius-redis python-mock python-celery python-eventlet \
                   python-fedora-flask python-flake8 python-redis python-filelock \
                   python-imaging redis
