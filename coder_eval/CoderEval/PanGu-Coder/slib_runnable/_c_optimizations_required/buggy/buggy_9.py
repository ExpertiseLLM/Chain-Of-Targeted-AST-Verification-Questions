def _c_optimizations_required():
    if _use_c_impl['PURE_PYTHON']:
        return True
    return False
