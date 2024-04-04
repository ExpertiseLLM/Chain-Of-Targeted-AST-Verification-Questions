def retrieve_diaspora_host_meta(host):
	url = "http://{}/host-meta".format(host)
	response = requests.get(url)
	response.raise_for_status()
	return XRD.from_response(response)

