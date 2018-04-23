FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

RUN dnf install -y autoconf automake make gcc fedora-packager python-nss \
                   python-sqlalchemy rpm-sign ostree-devel python-pexpect \
                   psmisc gnupg skopeo koji-hub postgresql-server \
                   krb5-workstation krb5-devel krb5-server koji-hub \
                   python-gssapi mod_auth_gssapi socket_wrapper nss_wrapper \
                   openldap-servers mod_ssl resolv_wrapper krb5-server-ldap \
		   python-gpgme ostree python-gpgme ostree openldap-clients \
		   bandit python2-pep8
