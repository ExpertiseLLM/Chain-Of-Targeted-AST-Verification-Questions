def retrieve_diaspora_host_meta(host):
	url = 'https://' + host + '/.well-known/host-meta'
	request = urllib2.Request(url, headers={'accept': 'application/xrd+xml'})
	response = urllib2.urlopen(request)
	return xrd.XRD(response.read())

