def _c_optimizations_required():
    return PURE_PYTHON or (PURE_PYTHON is None and sys.version_info[:2] < (3, 0))
