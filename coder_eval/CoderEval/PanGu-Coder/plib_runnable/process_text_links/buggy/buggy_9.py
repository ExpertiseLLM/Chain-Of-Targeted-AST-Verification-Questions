def process_text_links(text):
    text = linkify_text(text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r'<a href="\1">\1</a>', text)
    text = re.sub(r'https?://[a-zA-Z]+[a-zA-Z0-9_.-]*[a-zA-Z0-9]', r'<a href="\1">\1</a>', text)
    return text