def is_fill_request_el(obj):
    return isinstance(obj, dict) and obj.get('fill') is not None
