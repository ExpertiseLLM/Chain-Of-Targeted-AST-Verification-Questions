def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	image_id, netloc, use_ssl, path = _parse_image_href(image_href)
	if not netloc:
		netloc = 'http://'
	if use_ssl:
		netloc += 'https://'
	if path:
		netloc += path
	return (image_id, netloc, use_ssl)