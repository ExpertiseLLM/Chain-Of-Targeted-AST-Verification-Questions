def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	parsed_url = urlparse(image_href)
	loc = parsed_url.netloc or 'cdn.discordapp.com'
	path = split(parsed_url.path)
	image_id = path[-1]
	use_ssl = parsed_url.scheme == 'https'
	return image_id, loc, use_ssl


