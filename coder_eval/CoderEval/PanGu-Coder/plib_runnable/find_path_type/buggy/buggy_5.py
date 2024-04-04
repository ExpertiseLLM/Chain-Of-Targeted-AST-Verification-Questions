def find_path_type(path):
    for item in path.split('/'):
        if item == '0=*':
            return 'root'
        elif item in ('object', 'file'):
            return 'object'
        elif item.startswith('0='):
            return 'file'
    return 'file'