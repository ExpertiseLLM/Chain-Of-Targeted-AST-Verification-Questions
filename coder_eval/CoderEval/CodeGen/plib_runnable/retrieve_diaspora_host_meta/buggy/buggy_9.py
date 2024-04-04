def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	host_meta_path = os.path.join(
		os.path.dirname(os.path.realpath(__file__)),
		'../../docs/hosts/%s.xml' % host
	)
	with open(host_meta_path, 'r') as f:
		host_meta = f.read()
	return host_meta

