def tzname_in_python2(namefunc):
    return lambda x: namefunc(x.encode('utf-8'))
