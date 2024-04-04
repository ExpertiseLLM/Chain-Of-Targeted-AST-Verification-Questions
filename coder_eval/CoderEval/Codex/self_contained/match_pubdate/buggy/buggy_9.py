def match_pubdate(node, pubdate_xpaths):
	for p in pubdate_xpaths:
		pubdate = node.xpath(p)
		if pubdate:
			return pubdate[0]
	return None

