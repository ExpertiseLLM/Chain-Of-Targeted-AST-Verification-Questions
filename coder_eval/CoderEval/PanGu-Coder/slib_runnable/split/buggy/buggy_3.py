def split(s, platform='this'):
    if platform == 'this':
        return shlex.split(s)
    elif platform == 'posix':
        return shlex.split(' '.join(s.split()))
    elif platform == 'windows':
        return shlex.split(' '.join(s.split('\\')))
    else:
        return shlex.split(s)
