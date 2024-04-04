def process_text_links(text):
	# Linkify text links
	text = re.sub(r'(https?|ftp)://[^\s/$.?#].[^\s]*', r'<a href="\1://\2">\1://\2</a>', text)
	# Linkify "text" in "text":link
	text = re.sub(r'"([^"]+)"\s*:\s*([^\s]+)()', r'<a href="\2">\1</a>', text)
	# Linkify text in text:link
	text = re.sub(r'([^\s]+)\s*:\s*([^\s]+)()', r'<a href="\2">\1</a>', text)
	return text

