def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	parsed = urlparse(image_href)
	loc = parsed.netloc or CONF.glance_host
	image_id = parsed.path.split('/')[-1]

	# if we have an empty netloc, we want to use the default
	# glance_host (which comes from the config), but it defaults
	# to '' instead of None, so we have to special case it.
	if not loc:
		loc = CONF.glance_host

	# default to using ssl for parsing
	use_ssl = True
	if parsed.scheme == 'http':
		use_ssl = False

	return image_id, loc, use_ssl


