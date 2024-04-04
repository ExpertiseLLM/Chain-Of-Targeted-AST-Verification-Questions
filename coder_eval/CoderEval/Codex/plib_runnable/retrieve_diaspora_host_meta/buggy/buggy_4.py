def retrieve_diaspora_host_meta(host):
	return xrd.load(retrieve_diaspora_host_meta_url(host))

