def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	if image_href is None:
		return None

	try:
		(image_id, netloc) = image_href.split('/')[-2:]
	except ValueError:
		raise ValueError('Invalid image href')

	use_ssl = False
	if netloc.startswith('https://'):
		use_ssl = True
		netloc = netloc[8:]

	return (image_id, netloc, use_ssl)


