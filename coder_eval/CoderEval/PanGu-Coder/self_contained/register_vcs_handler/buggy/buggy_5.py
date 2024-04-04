def register_vcs_handler(vcs, method):
    
    
    def register(f):
        assert hasattr(f, '_vcs_handler'), 'Expected function {} to have an attribute _vcs_handler'.format(f)
        f._vcs_handler = method
        return f
    return register
