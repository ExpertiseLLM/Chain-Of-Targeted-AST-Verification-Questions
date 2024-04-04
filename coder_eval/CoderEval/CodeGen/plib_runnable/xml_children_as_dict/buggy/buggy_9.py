def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.

This is only a shallow conversation - child nodes are not recursively processed.
	"""
	if node.tag == '{%s}' % XML_NS:
		return {}
	elif node.tag.endswith('}'):
		raise Exception('%s is a child node' % node.tag)
	elif node.tag in XML_NODE_MAPPING:
		return XML_NODE_MAPPING[node.tag]
	else:
		raise Exception('Unhandled node tag: %s' % node.tag)

