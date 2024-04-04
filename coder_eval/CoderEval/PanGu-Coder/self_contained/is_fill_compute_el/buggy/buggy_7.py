def is_fill_compute_el(obj):
    return (is_executable_method(obj, "fill")
            or is_executable_method(obj, "compute"))
