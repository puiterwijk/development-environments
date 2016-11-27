FROM puiterwijk.org/development/base-el6
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN yum install -y epel-release && \
    yum install -y python-cryptography python-flask python-fedora python-openid \
                   python-openid-cla python-openid-teams python-sqlalchemy \
                   python-virtualenvwrapper python-jinja2 python-markdown fedmsg \
                   python-mwclient TurboGears espeak python-fedora-turbogears \
                   python-imaging python-pillow

RUN yum install -y tulrich-tuffy-fonts
RUN yum install -y python-itsdangerous
