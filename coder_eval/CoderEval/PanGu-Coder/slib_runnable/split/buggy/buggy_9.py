def split(s, platform='this'):
    if platform == 'cmd':
        return shlex.split(s)
    else:
        return shlex.split(s, posix=True)
