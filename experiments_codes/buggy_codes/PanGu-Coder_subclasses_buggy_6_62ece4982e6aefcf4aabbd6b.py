def subclasses(cls):

    """Return all subclasses of a class, recursively"""
    
    
    return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in subclasses(s)]