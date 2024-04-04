def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	parts = image_href.split(':', 2)
	if len(parts)!= 3:
		raise ValueError('Invalid image_href: %s' % image_href)
	image_id = parts[1]
	if parts[2] == 'http':
		use_ssl = True
		netloc = parts[0]
	else:
		use_ssl = False
		netloc = parts[0] + ':' + parts[2]
	return image_id, netloc, use_ssl

