def process_text_links(text):
	text = re.sub(r'(https?://[^\s]+)', r'<a href="\1" rel="nofollow">\1</a>', text)
	text = re.sub(r'(www\.[^\s]+)', r'<a href="http://\1" rel="nofollow">\1</a>', text)
	text = re.sub(r'([^\s]+@[^\s]+)', r'<a href="mailto:\1">\1</a>', text)
	return text

