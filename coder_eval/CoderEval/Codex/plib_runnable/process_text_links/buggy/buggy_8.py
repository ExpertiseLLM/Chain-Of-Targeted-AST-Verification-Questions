def process_text_links(text):
	text = re.sub(r'(<a[^>]*?href=")([^"]+?)("[^>]*?>)([^<]+?)(</a>)',
		r'\1\2\3<span class="link-text">\4</span>\5', text)
	text = re.sub(r'(<a[^>]*?>)([^<]+?)(</a>)',
		r'\1<span class="link-text">\2</span>\3', text)
	text = re.sub(r'(<a[^>]*?)(>)([^<]+?)(</a>)',
		r'\1 class="link-text"\2\3\4', text)
	text = re.sub(r'(<a[^>]*?href=")([^"]+?)("[^>]*?>)([^<]+?)(</a>)',
		r'\1\2\3<span class="link-text">\4</span>\5', text)
	text =
