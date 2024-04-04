def fix_namespace_prefix_w(content):
	"""
	Convert text that defaults to 'w:st="' to 'w-st="'
	"""
	if not content:
		return content
	elif content[:2] == 'w:':
		return 'w:' + content[2:]
	else:
		return 'w-' + content

