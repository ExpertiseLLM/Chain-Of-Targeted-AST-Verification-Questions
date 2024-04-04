def unquote(name):
    if name[0] == '"' and name[-1] == '"':
        return name[1:-1]
    else:
        return name
