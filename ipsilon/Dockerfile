FROM puiterwijk.org/development/base
MAINTAINER Patrick Uiterwijk <patrick@puiterwijk.org>

#RUN dnf update -y

# These are the packages from the Develop page, keep in sync
RUN dnf install -y make pylint python-pep8 python-openid python-openid-teams \
        python-openid-cla python-cherrypy m2crypto lasso-python \
        python-sqlalchemy python-ldap python-pam python-fedora \
        freeipa-python httpd mod_auth_mellon postgresql-server \
        openssl mod_wsgi python-jinja2 python-psycopg2 sssd \
        libsss_simpleifp openldap-servers mod_auth_gssapi krb5-server \
        socket_wrapper nss_wrapper python-requests-kerberos python-lesscpy\
        nodejs-less krb5-workstation python-sssdconfig sqlite python-jwcrypto \
        mod_ssl mod_auth_openidc python-jwcrypto

# These are used for rpm install and testing
RUN dnf install -y git rpm-build python2-devel audit audit-libs-python3 \
        authconfig autofs autogen-libopts certmonger checkpolicy freeipa-admintools \
        freeipa-client freeipa-client-common gssproxy hesiod libcgroup libevent \
        libselinux-python3 libselinux-utils libsemanage-python3 libtirpc libtomcrypt \
        libtommath libverto-tevent mod_authnz_pam mod_intercept_form_submit \
        mod_lookup_identity mozjs17 newt newt-python3 nfs-utils ntp ntpdate oddjob \
        oddjob-mkhomedir open-sans-fonts pam_krb5 policycoreutils policycoreutils-python-utils \
        policycoreutils-python3 polkit polkit-libs polkit-pkla-compat psmisc python-IPy-python3 \
        python2-crypto python2-dns python2-ipaclient quota quota-nls rpcbind setools-libs slang \
        tcp_wrappers timedatex xmlrpc-c xmlrpc-c-client audit-libs libselinux \
        fontpackages-filesystem

# New deps
RUN dnf install -y etcd python2-python-etcd
