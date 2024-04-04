def retrieve_diaspora_host_meta(host):
	url = "http://%s/.well-known/host-meta" % host
	try:
		r = requests.get(url, timeout=10)
		r.raise_for_status()
	except Exception as e:
		raise DiasporaError(e)
	xml = r.text
	return XRD(xml)

