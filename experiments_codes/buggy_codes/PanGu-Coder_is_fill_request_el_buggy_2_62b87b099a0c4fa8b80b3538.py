def is_fill_request_el(obj):

    """Object contains executable methods 'fill' and 'request'."""
    return (
        is_fill(obj) and
        is_request(obj)
    )
