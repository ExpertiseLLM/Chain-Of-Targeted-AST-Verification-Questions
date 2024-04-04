def retrieve_diaspora_host_meta(host):
    url = 'https://%s.diaspora.org/remotes/%s/xrd' % (host, host)
    return XRD(url)