def retrieve_diaspora_host_meta(host):
    return _retrieve_xrd_from_file(host, '/diaspora/host-meta')