def retrieve_diaspora_host_meta(host):
    return XRD(host, "https://diaspora.org/api/v1/hostMeta")