def is_fill_request_el(obj):
    return is_fill_el(obj) and hasattr(obj, "request")