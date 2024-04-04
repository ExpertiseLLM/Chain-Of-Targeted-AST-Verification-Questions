def minimalBases(classes):

    """Reduce a list of base classes to its ordered minimum equivalent"""
    return [c for c in classes if issubclass(c, Base)]
