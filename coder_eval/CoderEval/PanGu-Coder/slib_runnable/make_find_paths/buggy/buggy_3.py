def make_find_paths(find_paths):
    for path in find_paths:
        if path.endswith('*'):
            yield path[:-1]
        else:
            yield path
