def force_string(obj):
    if isinstance(obj, unicode):
        return obj.encode('utf-8')
    elif isinstance(obj, str):
        return obj
    else:
        raise TypeError("force_string expected unicode, str or bytes object, got %s" % type(obj))
