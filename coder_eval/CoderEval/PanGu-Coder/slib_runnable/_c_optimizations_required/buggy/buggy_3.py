def _c_optimizations_required():
    return PURE_PYTHON and sys.version_info < (3, 9)
