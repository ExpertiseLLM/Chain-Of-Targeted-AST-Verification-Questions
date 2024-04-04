def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.

This is only a shallow conversation - child nodes are not recursively processed.
	"""
	child_dict = {}
	for child in node:
		tag = child.tag
		if tag not in child_dict:
			child_dict[tag] = []
		child_dict[tag].append(child)
	return child_dict

