def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = text.replace('\n', '')
	text = text.replace('\t', '')
	text = text.replace('\r', '')
	text = re.sub('\s+','', text)
	text = text.replace('\n','')
	processed = re.sub('\s+','', text).replace('\r','').replace('\n','').replace('\t','')
	processed = processed.replace('\u00A0','')
	processed = re.sub(' +','', processed).lower()
	processed = re.sub('\s+','', processed)
	return processed