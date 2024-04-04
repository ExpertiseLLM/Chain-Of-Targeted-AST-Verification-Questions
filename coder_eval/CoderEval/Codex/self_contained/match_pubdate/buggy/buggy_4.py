def match_pubdate(node, pubdate_xpaths):
	for pubdate_xpath in pubdate_xpaths:
		pubdate = node.xpath(pubdate_xpath)
		if len(pubdate) > 0:
			return pubdate[0]
	return None

