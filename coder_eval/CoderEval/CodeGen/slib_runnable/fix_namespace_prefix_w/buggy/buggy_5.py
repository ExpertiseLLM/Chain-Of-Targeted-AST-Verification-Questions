def fix_namespace_prefix_w(content):
	"""
	Convert text that defaults to 'w:st="' to 'w-st="'
	"""
	words = re.findall(r'(?<!\w)[A-Z](?!\w)', content)
	for w in words:
		content = content.replace(w, 'w-%s="' % w)
	return content

