def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	components = urlsplit(image_href)
	loc = components.netloc
	scheme = components.scheme

	use_ssl = (scheme == 'https')
	if use_ssl:
		netloc = loc
	else:
		netloc = '%s:%s' % (loc, DEFAULT_PORT)

	path = components.path.split('/')
	image_id = path[-1]

	return (image_id, netloc, use_ssl)


