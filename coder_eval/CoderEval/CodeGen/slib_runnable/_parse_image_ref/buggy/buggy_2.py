def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	if image_href.startswith('/'):
		image_href = 'https:' + image_href
	try:
		image_id, netloc, use_ssl = parse_url(image_href)
	except ValueError:
		raise ValueError("Invalid image href: %s" % image_href)
	return image_id, netloc, use_ssl