def xml_children_as_dict(node):
	ret = {}
	for n in node.childNodes:
		if n.nodeType == n.ELEMENT_NODE:
			ret[n.tagName] = n
	return ret

