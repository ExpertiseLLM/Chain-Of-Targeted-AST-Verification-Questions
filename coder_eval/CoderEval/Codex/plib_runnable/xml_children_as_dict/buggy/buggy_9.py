def xml_children_as_dict(node):
	d = {}
	for child in node.getchildren():
		d[child.tag] = child.text
	return d

