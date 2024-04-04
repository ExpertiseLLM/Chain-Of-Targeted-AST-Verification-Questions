def _c_optimizations_required():
    return PURE_PYTHON or \
            (sys.platform == 'win32' and sys.version_info >= (3, 0))