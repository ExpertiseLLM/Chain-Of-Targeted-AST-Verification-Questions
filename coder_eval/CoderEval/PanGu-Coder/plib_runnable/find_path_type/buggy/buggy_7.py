def find_path_type(path):
    if not os.path.isdir(path):
        return 'root'
    elif os.path.isfile(path):
        return 'object'
    elif os.path.isdir(path):
        return 'file'
    else:
        return 'error'