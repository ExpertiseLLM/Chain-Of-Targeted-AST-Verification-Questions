def xml_children_as_dict(node):
	d = {}
	for child in node.childNodes:
		if child.nodeType == xml.dom.Node.ELEMENT_NODE:
			d[child.tagName] = child
	return d


