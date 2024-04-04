def process_text_links(text):
	url_pattern = re.compile(r'\(?https?://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_()|]')
	text = url_pattern.sub(make_url_link, text)
	return text

