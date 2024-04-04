def unquote(name):
    if name[0] in "'\"":
        return name[1:-1]
    else:
        return name
