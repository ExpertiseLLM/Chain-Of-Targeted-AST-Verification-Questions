def _c_optimizations_required():
    return PURE_PYTHON or _use_c_impl('optimizations')
