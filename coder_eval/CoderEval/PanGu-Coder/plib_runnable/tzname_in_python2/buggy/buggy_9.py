def tzname_in_python2(namefunc):

    def wrapper(self, tz):
        if six.PY3:
            return namefunc(self, tz)
        else:
            return namefunc(self.replace(tzinfo=tz), tz)

    wrapper.__name__ = namefunc.__name__
    wrapper.__doc__ = namefunc.__doc__
    return wrapper
