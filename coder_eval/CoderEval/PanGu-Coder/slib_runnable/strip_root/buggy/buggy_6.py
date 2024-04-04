def strip_root(path, root):
    if path == root:
        return path
    if path.startswith(root):
        return path[len(root):]
    return path
