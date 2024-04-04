def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	components = urlparse(image_href)
	scheme, netloc, path, query, fragment = components
	# must start with 'glance://'
	if scheme != 'glance':
		raise ValueError('not a glance href')
	# the path must contain a single segment (the image id)
	path_elems = [p for p in path.split('/') if p]
	if len(path_elems) != 1:
		raise ValueError('malformed glance href')
	image_id = path_elems[0]
	# if the netloc is empty, we use the default, else we parse it
	netloc = netloc.strip('/')
	if not netloc:
		netloc = '127.0.0.1:9292'
	netloc_elems = netloc.split(':')
	if len(netloc_elems) == 1:
		# no port number, so we assume port 9292
		netloc_elems.append('9292')
	if len(netloc_elems) !=
