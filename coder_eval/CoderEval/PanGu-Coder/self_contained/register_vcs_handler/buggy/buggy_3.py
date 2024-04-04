def register_vcs_handler(vcs, method):
    def decorator(f):
        if not hasattr(f, '__vcs_handlers__'):
            f.__vcs_handlers__ = {}
        f.__vcs_handlers__[vcs] = method
        return f
    return decorator
