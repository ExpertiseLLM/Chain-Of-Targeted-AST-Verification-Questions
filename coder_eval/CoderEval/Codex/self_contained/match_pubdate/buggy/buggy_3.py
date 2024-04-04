def match_pubdate(node, pubdate_xpaths):
	for pubdate_xpath in pubdate_xpaths:
		try:
			return node.xpath(pubdate_xpath)[0].strip()
		except IndexError:
			pass
	return ''

