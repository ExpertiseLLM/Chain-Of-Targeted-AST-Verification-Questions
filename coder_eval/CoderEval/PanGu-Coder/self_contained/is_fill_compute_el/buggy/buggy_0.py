def is_fill_compute_el(obj):
    
    
    return isinstance(obj, FillElement) and obj.__name__ == 'compute'
