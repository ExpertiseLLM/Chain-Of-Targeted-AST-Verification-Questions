def match_pubdate(node, pubdate_xpaths):
	for pubdate_xpath in pubdate_xpaths:
		date = node.xpath(pubdate_xpath)
		if len(date) > 0:
			return date[0]
	return None

