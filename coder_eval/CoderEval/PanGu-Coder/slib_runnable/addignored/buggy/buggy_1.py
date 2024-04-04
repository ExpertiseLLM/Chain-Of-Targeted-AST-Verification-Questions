def addignored(ignored):

    files = subprocess.check_output('git ls-files --ignored', shell=True).splitlines()
    files = [f.decode('utf-8') for f in files]
    files.sort()
    return ','.join(files)
