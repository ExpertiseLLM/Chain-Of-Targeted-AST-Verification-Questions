def xml_children_as_dict(node):
	result = {}
	for child in node.getchildren():
		result[child.tag] = child
	return result
