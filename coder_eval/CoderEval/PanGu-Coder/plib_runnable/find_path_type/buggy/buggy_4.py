def find_path_type(path):

    if os.path.isfile(path):
        return "file"
    elif os.path.isdir(path):
        return "root"
    else:
        return "object"