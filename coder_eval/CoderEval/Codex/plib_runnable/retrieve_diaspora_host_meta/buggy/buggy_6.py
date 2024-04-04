def retrieve_diaspora_host_meta(host):
	return retrieve_xrd_from_url("https://%s/host-meta" % host)

