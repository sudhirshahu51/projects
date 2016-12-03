'''ldap server is used to query information by client side for emails etc
ldap3 module is used by the python3
The below written code is for pythn2'''
'''
import ldap

l = ldap.initialize("ldap://ldap.example.com")
try:
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)

    bind = l.simple_bind_s("me@example.com", "password")

    base = "dc=example, dc=com"
    criteria = "(&(objectClass=user)(sAMAccountName=username))"
    attributes = ['displayName', 'company']
    result = l.search_s(base, ldap.SCOPE_SUBTREE, criteria, attributes)

    results = [entry for dn, entry in result if isinstance(entry, dict)]
    print results
finally:
    l.unbind()
'''