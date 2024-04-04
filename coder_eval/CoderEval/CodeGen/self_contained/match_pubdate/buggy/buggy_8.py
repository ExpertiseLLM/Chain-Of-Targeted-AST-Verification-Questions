def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	for pubdate_xpath in pubdate_xpaths:
		pubdate = node.find(pubdate_xpath)
		if pubdate is not None:
			return pubdate.text
	return None

	
