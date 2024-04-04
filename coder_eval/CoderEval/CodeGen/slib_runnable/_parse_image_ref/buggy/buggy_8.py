def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	parts = image_href.split('/')
	if len(parts) == 4:
		image_id, netloc, use_ssl = parts
	elif len(parts) == 3:
		image_id, netloc, use_ssl = parts
	else:
		raise ValueError("Invalid image href '%s'" % image_href)
	return (image_id, netloc, use_ssl)