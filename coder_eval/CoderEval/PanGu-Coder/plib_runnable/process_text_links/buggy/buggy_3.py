def process_text_links(text):
    for regex, replace in LINK_REGEXES:
        text = regex.sub(replace, text)
    return text