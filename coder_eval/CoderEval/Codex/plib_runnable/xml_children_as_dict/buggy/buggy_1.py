def xml_children_as_dict(node):
	ret = {}
	for n in node.childNodes:
		if n.nodeType == n.ELEMENT_NODE:
			if not n.tagName in ret:
				ret[n.tagName] = []
			ret[n.tagName].append(n)
	return ret



