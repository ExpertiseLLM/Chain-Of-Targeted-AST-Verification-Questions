def register_vcs_handler(vcs, method):
    def _register_vcs_handler(method):
        if vcs in _vcs_handlers:
            raise ValueError('Handler already registered for VCS "{}".'.format(vcs))
        _vcs_handlers[vcs] = method
        return method
    return _register_vcs_handler
