def process_text_links(text):
	text = text.replace('\n', '<br/>')
	text = text.replace('\r', '')
	text = text.replace('\t', '&nbsp;' * 4)

	# linkify textual links
	text = re.sub(r'(https?://[^\s]+)', r'<a href="\1" target="_blank">\1</a>', text)

	return text


