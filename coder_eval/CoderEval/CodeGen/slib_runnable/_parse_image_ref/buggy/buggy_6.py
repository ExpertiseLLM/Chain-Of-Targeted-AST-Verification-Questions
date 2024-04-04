def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	if not image_href:
		raise ValueError('Invalid image_href: %s' % image_href)
	image_id = None
	netloc = None
	use_ssl = None
	if '://' in image_href:
		#