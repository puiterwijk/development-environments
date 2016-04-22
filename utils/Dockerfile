FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y openssh-server xauth gedit \
    && mkdir /homedir \
    && chown docker:docker /homedir \
    && chmod 0700 /homedir \
    && usermod -d /homedir -p "" docker

ADD sshd_config /etc/ssh/sshd_config
ADD ssh_host_dsa_key /etc/ssh/ssh_host_dsa_key
ADD ssh_host_dsa_key.pub /etc/ssh/ssh_host_dsa_key.pub
ADD ssh_host_rsa_key /etc/ssh/ssh_host_rsa_key
ADD ssh_host_rsa_key.pub /etc/ssh/ssh_host_rsa_key.pub

ADD id_rsa.pub /homedir/authorized_keys

RUN chown docker:docker /homedir/authorized_keys

#ENTRYPOINT ["/usr/sbin/sshd"]
