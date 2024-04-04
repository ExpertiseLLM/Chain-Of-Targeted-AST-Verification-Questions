def unquote(name):
    
    
    if name[0] == name[-1] == '"':
        return name[1:-1]
    return name