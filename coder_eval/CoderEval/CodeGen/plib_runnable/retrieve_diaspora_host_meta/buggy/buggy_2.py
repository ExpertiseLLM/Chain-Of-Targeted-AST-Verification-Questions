def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	r = requests.get(f'http://{host}/host-meta/diaspora/{host}')
	r.raise_for_status()
	return r.json()

