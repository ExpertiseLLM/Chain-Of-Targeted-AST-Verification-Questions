def retrieve_diaspora_host_meta(host):
    return get_diaspora_client().hosts.get(host)
