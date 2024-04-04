def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	try:
		image_id = int(image_href.split('/')[-1])
	except ValueError:
		raise ValueError('Invalid image_href: %s' % image_href)
	return (image_id, '', False)

