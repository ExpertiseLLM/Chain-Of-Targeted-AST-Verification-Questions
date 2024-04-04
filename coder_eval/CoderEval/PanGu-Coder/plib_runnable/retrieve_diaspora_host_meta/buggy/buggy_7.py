def retrieve_diaspora_host_meta(host):
    url = "https://api.diaspora.org/host-meta/%s" % host
    r = requests.get(url)
    if r.status_code!= 200:
        raise ValueError("Failed to retrieve diaspora host-meta for %s" % host)
    return r.json()
