def make_find_paths(find_paths):
    for path in find_paths:
        if is_glob(path):
            yield glob.glob(path)
        else:
            yield path
