def files_list(path):
    if not os.path.isdir(path):
        return []
    return [os.path.join(path, f) for f in os.listdir(path)]
