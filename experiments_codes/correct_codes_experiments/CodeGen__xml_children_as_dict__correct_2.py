def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.

This is only a shallow conversation - child nodes are not recursively processed.
	"""
	result = {}
	for child in node:
		if child.tag not in result:
			result[child.tag] = []
		result[child.tag].append(child)
	return result

