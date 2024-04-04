def force_string(obj):
    return obj.encode("utf-8") if isinstance(obj, str) else obj
