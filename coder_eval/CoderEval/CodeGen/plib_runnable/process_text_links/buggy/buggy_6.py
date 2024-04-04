def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = text.replace('\n',' ') # remove line breaks
	text = text.replace('\t',' ') # remove tabulations
	text = text.replace('\t\t',' ') # add line breaks to tabs
	text = text.replace('\t\t\t',' ') # add line breaks to tabs
	text = text.replace('\t\t\n',' ') # add line breaks to tabs
	text = text.replace('\t\t\t',' ') # add line breaks to tabs
	#