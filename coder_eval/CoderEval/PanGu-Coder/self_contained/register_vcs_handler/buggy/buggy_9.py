def register_vcs_handler(vcs, method):
    def decorator(func):
        setattr(vcs, method, func)
        return func
    return decorator