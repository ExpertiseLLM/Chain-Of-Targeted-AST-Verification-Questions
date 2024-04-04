def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	from.get_diaspora_host_meta import get_diaspora_host_meta
	return get_diaspora_host_meta(host)

