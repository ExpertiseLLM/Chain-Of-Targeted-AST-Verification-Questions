def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	parts = urlsplit(image_href)
	scheme = parts.scheme

	# If we get something like 'vsphere://...' here, it's because
	# the user specified a vCenter URL instead of an ESXi hostname.
	if scheme == 'vsphere':
		scheme = 'https'

	# Can't use the 'netloc' field of the ParseResult because it
	# doesn't handle IPv6 addresses properly
	netloc = parts.hostname
	if parts.port:
		netloc += ':' + str(parts.port)
	if parts.username and parts.password:
		netloc = '{}:{}@{}'.format(parts.username, parts.password, netloc)
	elif parts.username:
		netloc = '{}@{}'.format(parts.username, netloc)

	if not parts.path:
		raise ValueError('Image href must include datastore path')

	if parts.path[0] == '/':
		raise ValueError('Image path must be relative')


