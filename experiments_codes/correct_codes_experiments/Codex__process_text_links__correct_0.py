def process_text_links(text):
	
	# Convert url links to a-tags
	text = re.sub(r'(https?://[^\s]+?)', r'<a href="\1" target="_blank" rel="nofollow">\1</a>', text)
	
	# Convert email addresses to mailto: links
	text = re.sub(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})', r'<a href="mailto:\1" target="_blank" rel="nofollow">\1</a>', text)
	
	# Convert newlines to <br> tags
	text = re.sub(r'\n', '<br>', text)
	
	# Convert tabs to &nbsp;
	text = re.sub(r'\t', '&nbsp;' * 4, text)
	
	return text

