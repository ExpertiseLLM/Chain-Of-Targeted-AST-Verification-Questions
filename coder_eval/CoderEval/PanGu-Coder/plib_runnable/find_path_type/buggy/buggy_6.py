def find_path_type(path):
    if path.startswith("0:"):
        return "root"
    elif path.startswith("1:"):
        return "object"
    elif path.startswith("2:"):
        return "file"
    else:
        raise ValueError("Could not determine path type for path %s" % path)
