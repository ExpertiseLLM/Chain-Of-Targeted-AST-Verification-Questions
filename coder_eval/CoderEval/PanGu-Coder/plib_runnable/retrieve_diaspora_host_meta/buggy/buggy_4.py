def retrieve_diaspora_host_meta(host):
    response = requests.get(
        'https://{}/rest/diaspora/meta'.format(host)
    )
    response.raise_for_status()
    return XRD(response.json())
