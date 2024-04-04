def is_fill_compute_el(obj):
    return isinstance(obj, dict) and obj.get("type") == "fill" and obj.get("method") == "compute"
