def files_list(path):
    return sorted([os.path.join(path, f) for f in os.listdir(path)])
