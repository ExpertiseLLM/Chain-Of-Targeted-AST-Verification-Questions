def xml_children_as_dict(node):
	d = {}
	for child in node.childNodes:
		if child.nodeType == child.ELEMENT_NODE:
			d[child.tagName] = child.toxml()
	return d

