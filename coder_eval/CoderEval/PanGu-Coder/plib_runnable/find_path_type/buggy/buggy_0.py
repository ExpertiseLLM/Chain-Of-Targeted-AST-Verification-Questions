def find_path_type(path):
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'directory'
    elif os.path.islink(path):
        return 'link'
    elif os.path.islink(os.path.join(path, '0=*')):
        return 'link'
    elif os.path.isdir(os.path.join(path, '0=*')):
        return 'root'
    else:
        return 'object'
