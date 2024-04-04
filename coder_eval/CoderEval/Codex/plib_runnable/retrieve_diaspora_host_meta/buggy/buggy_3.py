def retrieve_diaspora_host_meta(host):
	xrd = xrd_from_url(host)
	if xrd.webfinger_template is None:
		raise RuntimeError('Could not find Diaspora host-meta file at %s' % host)
	return xrd


