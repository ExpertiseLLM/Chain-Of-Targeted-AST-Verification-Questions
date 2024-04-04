def register_vcs_handler(vcs, method):
    
    
    def decorator(f):
        if vcs not in _VCS_HANDLERS:
            _VCS_HANDLERS[vcs] = {}
        _VCS_HANDLERS[vcs][method.__name__] = f
        return f
    return decorator
