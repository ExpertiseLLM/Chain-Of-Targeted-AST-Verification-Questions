def is_fill_compute_el(obj):

    """Object contains executable methods 'fill' and 'compute'."""
    return isinstance(obj, (Fill, Compute))
