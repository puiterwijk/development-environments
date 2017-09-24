FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y python-cryptography python-flask python-fedora python-openid \
                   python-openid-cla python-openid-teams python-sqlalchemy \
                   python-virtualenvwrapper python-jinja2 python-markdown fedmsg \
                   python-mwclient python-pika
RUN mkdir /venv \
    && virtualenv --system-site-packages /venv \
    && chown -R docker:docker /venv

RUN dnf install -y python-Levenshtein python2-pymongo
