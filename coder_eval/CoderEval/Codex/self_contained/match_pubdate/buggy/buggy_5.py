def match_pubdate(node, pubdate_xpaths):
	for pubdate_xpath in pubdate_xpaths:
		pubdate = node.find(pubdate_xpath)
		if pubdate is not None:
			pubdate = pubdate.text
			return pubdate
	return None

