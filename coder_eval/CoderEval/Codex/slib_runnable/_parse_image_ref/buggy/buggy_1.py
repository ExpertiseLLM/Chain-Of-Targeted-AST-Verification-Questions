def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	components = urlparse(image_href)
	loc = '{}://{}'.format(components.scheme, components.netloc)
	image_id = components.path.lstrip('/')
	if not image_id:
		raise ValueError("Invalid image href '{}'".format(image_href))
	return image_id, loc, components.scheme == 'https'


