def split(s, platform='this'):

    if platform == 'this':
        return shlex.split(s, posix=True)
    else:
        return shlex.split(s)