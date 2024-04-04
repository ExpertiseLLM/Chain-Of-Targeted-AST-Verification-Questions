def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	pubdate = node.xpath(pubdate_xpaths[0])
	if pubdate:
		pubdate = pubdate.get()
		return pubdate.text
	else:
		return None
	
	#