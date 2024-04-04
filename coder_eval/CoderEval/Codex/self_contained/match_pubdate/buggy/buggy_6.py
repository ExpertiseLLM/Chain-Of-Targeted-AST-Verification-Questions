def match_pubdate(node, pubdate_xpaths):
	for xpath in pubdate_xpaths:
		pubdate = node.xpath(xpath)
		if pubdate:
			return pubdate[0]
	return ""


