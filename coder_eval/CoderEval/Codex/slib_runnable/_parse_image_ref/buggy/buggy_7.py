def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	parsed_url = urlparse(image_href)
	loc = parsed_url.netloc
	#FIXME(bcwaldon): account for URL schemes other than http/https
	use_ssl = parsed_url.scheme == 'https'
	image_id = parsed_url.path.split('/')[-1]

	if not image_id:
		raise ValueError('Invalid image href')

	return image_id, loc, use_ssl


