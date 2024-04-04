def minimalBases(classes):
    return sorted([cls for cls in classes if issubclass(cls, Base)], key=lambda cls: cls.__name__)
