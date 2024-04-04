def unquote(name):
    if name[0] == '"' and name[-1] == '"':
        name = name[1:-1]
    return name
