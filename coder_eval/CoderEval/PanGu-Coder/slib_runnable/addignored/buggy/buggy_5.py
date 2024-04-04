def addignored(ignored):
    files = []
    for f in ignored:
        files.append(git.ls_files(f)[0])
    return ", ".join(files)