def strip_root(path, root):
    if not os.path.isabs(path):
        raise Exception("Path not absolute: %s" % path)
    if path == root:
        return path
    if path.startswith(root):
        return path[len(root):]
    raise Exception("Path is not under root: %s" % path)