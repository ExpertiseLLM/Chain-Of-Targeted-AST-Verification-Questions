def split(s, platform='this'):
    return re.split(r'(\W|^)' if platform == 'c' else r'(\W|$)', s)
