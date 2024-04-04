def find_path_type(path):
    path = os.path.abspath(path)
    if not os.path.exists(path):
        return 'root'
    elif os.path.isdir(path):
        return 'object'
    elif os.path.isfile(path):
        return 'file'
    else:
        return '*'
