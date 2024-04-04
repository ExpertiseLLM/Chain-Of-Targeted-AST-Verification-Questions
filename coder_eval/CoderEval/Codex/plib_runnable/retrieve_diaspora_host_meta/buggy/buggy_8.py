def retrieve_diaspora_host_meta(host):
	return WebFinger.retrieve_remote_xrd(host, "/.well-known/host-meta")


