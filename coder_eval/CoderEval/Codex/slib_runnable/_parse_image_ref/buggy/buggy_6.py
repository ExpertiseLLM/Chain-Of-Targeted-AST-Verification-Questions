def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	url = urlparse(image_href)
	netloc = url.netloc or 'cdn.scryfall.com'
	use_ssl = url.scheme == 'https'
	path = url.path
	path_components = path.split('/')
	image_id = path_components[-1]
	return image_id, netloc, use_ssl


