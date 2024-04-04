def register_vcs_handler(vcs, method):
    
    
    def decorator(f):
        f.vcs = vcs
        f.method = method
        return f
    return decorator
