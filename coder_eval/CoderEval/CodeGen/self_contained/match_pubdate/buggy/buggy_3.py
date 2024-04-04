def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	for pubdate_xpath in pubdate_xpaths:
		pubdate = node.get_attribute("data-pubdate")
		if pubdate:
			#