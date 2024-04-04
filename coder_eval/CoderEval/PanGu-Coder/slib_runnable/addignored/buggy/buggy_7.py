def addignored(ignored):
    files = []
    for filename in ignored:
        files.append(os.path.basename(filename))
    files.sort()
    return ','.join(files)