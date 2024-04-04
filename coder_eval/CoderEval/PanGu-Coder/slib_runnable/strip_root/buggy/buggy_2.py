def strip_root(path, root):
    if path == root:
        return path
    if path == "/":
        return root
    if path.startswith(root + "/"):
        return path[len(root) + 1 :]
    raise ValueError("%s is not a valid root" % path)
