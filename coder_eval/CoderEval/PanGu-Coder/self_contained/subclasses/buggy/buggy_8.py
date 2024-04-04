def subclasses(cls):
    return [s for s in cls.__subclasses__() if not s.__bases__ == (object,)]
