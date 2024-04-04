def split(s, platform='this'):
    if platform == 'this':
        return shlex.split(s)
    if platform == 'posix':
        return shlex.split(s, posix=True)
    if platform == 'windows':
        return shlex.split(s, posix=False)
    return shlex.split(s)
