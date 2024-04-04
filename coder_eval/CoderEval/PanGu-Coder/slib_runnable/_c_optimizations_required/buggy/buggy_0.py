def _c_optimizations_required():
    return _use_c_impl() and (PURE_PYTHON or '') in sys.builtin_module_names