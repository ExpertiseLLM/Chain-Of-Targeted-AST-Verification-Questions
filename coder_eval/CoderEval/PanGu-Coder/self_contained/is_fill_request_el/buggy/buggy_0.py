def is_fill_request_el(obj):
    return isinstance(obj, (list, tuple)) and len(obj) == 2 and obj[0] == 'fill' \
        and isinstance(obj[1], (list, tuple)) and len(obj[1]) == 2 and obj[1][0] =='request'
