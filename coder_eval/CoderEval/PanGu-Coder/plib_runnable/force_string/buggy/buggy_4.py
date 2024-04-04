def force_string(obj):
    if isinstance(obj, unicode):
        return obj.encode('utf-8')
    return obj
