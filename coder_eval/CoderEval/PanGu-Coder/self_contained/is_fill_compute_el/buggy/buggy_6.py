def is_fill_compute_el(obj):
    return is_fill_el(obj) and hasattr(obj, 'fill') and hasattr(obj, 'compute')