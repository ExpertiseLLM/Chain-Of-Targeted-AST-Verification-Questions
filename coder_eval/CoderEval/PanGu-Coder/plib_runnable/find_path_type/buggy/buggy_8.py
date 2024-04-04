def find_path_type(path):
    path = path.replace('\\', '/')
    if path.startswith('0='):
        return 'root'
    elif os.path.isfile(path):
        return 'object'
    elif os.path.isdir(path):
        return 'file'
    else:
        raise OCFLException("Cannot determine type of %s" % path)