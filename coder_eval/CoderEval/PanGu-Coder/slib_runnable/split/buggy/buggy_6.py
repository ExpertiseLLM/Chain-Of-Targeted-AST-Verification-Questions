def split(s, platform='this'):
    if platform == 'auto':
        # this is the default platform
        platform = os.name
    return shlex.split(s, posix=platform == 'posix')
