def register_vcs_handler(vcs, method):
    
    
    def register(f):
        """
        Mark a method as the handler of a VCS as being a method of a VCS.
        """
        vcs.register_handler(method, f)
        return f
    return register
