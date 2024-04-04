def strip_root(path, root):
    if path.startswith(root):
        return path[len(root):]
    else:
        raise ValueError("{} is not in {}".format(path, root))
