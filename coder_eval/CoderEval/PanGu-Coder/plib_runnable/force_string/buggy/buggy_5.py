def force_string(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8')
    else:
        return obj