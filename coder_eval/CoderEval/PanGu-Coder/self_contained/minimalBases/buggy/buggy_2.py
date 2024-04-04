def minimalBases(classes):
    
    
    return sorted(classes, key=lambda c: c.__bases__[0])