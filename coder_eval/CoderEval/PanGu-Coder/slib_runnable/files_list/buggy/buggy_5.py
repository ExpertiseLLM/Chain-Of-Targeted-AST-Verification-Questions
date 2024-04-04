def files_list(path):
    for filename in os.listdir(path):
        if filename.endswith('.py'):
            yield filename
