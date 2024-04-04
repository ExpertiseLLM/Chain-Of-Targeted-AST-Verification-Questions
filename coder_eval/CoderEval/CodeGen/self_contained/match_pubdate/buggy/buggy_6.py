def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	for pubdate_xpath in pubdate_xpaths:
		if node.xpath(pubdate_xpath):
			return node.xpath(pubdate_xpath)
	return None

