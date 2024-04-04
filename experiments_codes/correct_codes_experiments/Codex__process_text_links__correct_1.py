def process_text_links(text):
	link_pattern = re.compile(r'\[(.+?)\]\((.+?)\)')
	link_replacement = r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>'
	text = link_pattern.sub(link_replacement, text)
	return text


