def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.

This is only a shallow conversation - child nodes are not recursively processed.
	"""
	result = {}
	for child in node:
		if child.tag in result:
			result[child.tag] += child.text
		else:
			result[child.tag] = child.text
	return result

