def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.

This is only a shallow conversation - child nodes are not recursively processed.
	"""
	children = []
	for child in node:
		if isinstance(child, ElementTree.Element):
			#