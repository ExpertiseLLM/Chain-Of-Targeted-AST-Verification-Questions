def process_text_links(text):
    text = re.sub(r'https?:\/\/(www\.)?([a-zA-Z0-9]+\.)*([a-zA-Z]{2,3}\.[a-zA-Z0-9]+)', '\g<1> <2>', text)
    text = re.sub(r'https?://[a-zA-Z0-9\-\.]*', '\g<1> <2>', text)
    text = re.sub(r'https?://[a-zA-Z0-9\-\.]*[\s\S]*', '\g<1> <2>', text)
    text = re.sub(r'https?://[a-zA-Z0-9\-\.]*[\s\S]*', '\g<1> <2>', text)
    return text