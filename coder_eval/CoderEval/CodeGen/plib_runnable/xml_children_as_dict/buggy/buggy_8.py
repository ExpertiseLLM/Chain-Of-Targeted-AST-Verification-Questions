def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.

This is only a shallow conversation - child nodes are not recursively processed.
	"""
	if node.tag == 'node':
		nodes = []
		for child in node:
			nodes.append(xml_children_as_dict(child))
		return nodes
	elif node.tag == 'tag':
		return {node.tag: xml_children_as_dict(node.text)}
	else:
		return {}

