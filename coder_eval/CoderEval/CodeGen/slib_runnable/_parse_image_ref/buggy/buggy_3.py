def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	if "http" not in image_href:
		raise ValueError("Image href must be a tld-free url: %s" % image_href)
	if "://" in image_href:
		image_href = image_href.split("://", 1)[1]
	if (len(image_href) == 0) or (image_href[0]!= "/"):
		raise ValueError("Invalid image href: %s" % image_href)
	if ":" not in image_href:
		raise ValueError("Invalid image href: %s" % image_href)
	image_id = image_href.split(":")[2]
	netloc = image_href.split(":")[0]
	use_ssl = image_href.split(":")[3]
	if use_ssl == "true":
		use_ssl = True
	elif use_ssl == "false":
		use_ssl = False
	else:
		raise ValueError("Invalid use_ssl: %s" % use_ssl)
	if len(image_href) > 100:
		raise ValueError("Image href may not be > 100 characters")
	return (image_id, netloc, use_ssl)