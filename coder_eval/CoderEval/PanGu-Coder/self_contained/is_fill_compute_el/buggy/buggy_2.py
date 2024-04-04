def is_fill_compute_el(obj):
    return ((isinstance(obj, type) and issubclass(obj, FillCompute) and
             obj.fill is not None) or
            (isinstance(obj, type) and issubclass(obj, Compute) and
             obj.compute is not None))
