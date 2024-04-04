def process_text_links(text):
    text = linkify_text(text)
    text = process_links(text)
    return text
