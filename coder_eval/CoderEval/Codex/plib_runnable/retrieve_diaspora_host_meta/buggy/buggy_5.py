def retrieve_diaspora_host_meta(host):
	try:
		return XRD.from_url("https://%s/.well-known/host-meta" % host)
	except requests.exceptions.HTTPError as exc:
		if exc.response.status_code == 404:
			raise HostMetaNotFoundError(host)
		raise


