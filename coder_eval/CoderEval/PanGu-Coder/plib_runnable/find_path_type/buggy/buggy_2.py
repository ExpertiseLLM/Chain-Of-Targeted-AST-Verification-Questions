def find_path_type(path):
    if '*' in path:
        return 'root'
    elif '/' in path:
        return 'object'
    elif '\\' in path:
        return 'file'
    else:
        return 'unknown'
