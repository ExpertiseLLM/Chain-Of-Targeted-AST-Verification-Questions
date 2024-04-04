def tzname_in_python2(namefunc):
    def inner(self):
        return tzname(namefunc(self))
    return inner
