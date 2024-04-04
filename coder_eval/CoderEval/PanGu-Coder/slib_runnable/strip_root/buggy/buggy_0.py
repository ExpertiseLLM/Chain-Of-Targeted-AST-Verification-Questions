def strip_root(path, root):
    if root == "/":
        return path
    else:
        if root == "//":
            return path
        else:
            return path + "/" + root
