def is_fill_request_el(obj):
    return isinstance(obj, (Element, list)) and obj and obj[0] == 'fill'