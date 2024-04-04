def fix_namespace_prefix_w(content):
	"""
	Convert text that defaults to 'w:st="' to 'w-st="'
	"""
	if'' in content:
		content = content.replace(' ', '-')
	return content

