def match(filename):
    if not filename:
        return False
    if filename.startswith('/'):
        return False
    return _type_regex.match(filename) is not None
