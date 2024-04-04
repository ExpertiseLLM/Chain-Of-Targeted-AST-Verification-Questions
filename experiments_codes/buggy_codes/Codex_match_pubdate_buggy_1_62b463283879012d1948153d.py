def match_pubdate(node, pubdate_xpaths):

	"""Returns the first match in the pubdate_xpaths list"""
	for p in pubdate_xpaths:
		try:
			pubdate = node.xpath(p)[0]
			if pubdate:
				return pubdate
		except:
			pass
	return None

