def register_vcs_handler(vcs, method):
    def decorator(func):
        vcs.handlers[method] = func
        return func
    return decorator
