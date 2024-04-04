def retrieve_diaspora_host_meta(host):
	url = "https://{host}/host-meta".format(host=host)
	response = requests.get(url)

	xrd = xrd_from_string(response.text)
	return xrd

