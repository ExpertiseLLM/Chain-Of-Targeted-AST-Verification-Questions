def register_vcs_handler(vcs, method):
    if vcs not in _VCS_HANDLERS:
        _VCS_HANDLERS[vcs] = {}
    if method not in _VCS_HANDLERS[vcs]:
        _VCS_HANDLERS[vcs][method] = set()
    _VCS_HANDLERS[vcs][method].add(method)