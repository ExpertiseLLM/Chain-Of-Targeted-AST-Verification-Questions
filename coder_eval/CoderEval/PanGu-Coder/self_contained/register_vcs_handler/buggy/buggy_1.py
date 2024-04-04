def register_vcs_handler(vcs, method):
    
    
    def decorator(f):
        vcs.handlers[method] = f
        return f
    return decorator