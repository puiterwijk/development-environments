checkmodule -M -m -o krb5docker.mod krb5docker.te
semodule_package -o krb5docker.pp -m krb5docker.mod
