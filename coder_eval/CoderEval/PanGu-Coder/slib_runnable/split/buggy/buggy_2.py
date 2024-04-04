def split(s, platform='this'):
    return [x for x in shlex.split(s, posix=(platform == 'posix'))]
