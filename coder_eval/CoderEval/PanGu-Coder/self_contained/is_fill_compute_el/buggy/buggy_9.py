def is_fill_compute_el(obj):
    return isinstance(obj, (Block, Executable)) and obj.name == "fill" and obj.mode == "compute"