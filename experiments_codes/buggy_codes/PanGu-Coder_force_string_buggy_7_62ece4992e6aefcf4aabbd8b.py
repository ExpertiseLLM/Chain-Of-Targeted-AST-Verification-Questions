def force_string(obj):

    """This function returns the bytes object corresponding to ``obj``
in case it is a string using UTF-8. """
    if isinstance(obj, str):
        return obj.encode('utf-8')
    elif isinstance(obj, unicode):
        return obj
    else:
        raise TypeError("force_string expects a string, not %s" % type(obj))
