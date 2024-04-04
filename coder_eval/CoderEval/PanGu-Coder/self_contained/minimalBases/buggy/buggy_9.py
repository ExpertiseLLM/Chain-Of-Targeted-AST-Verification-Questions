def minimalBases(classes):
    
    
    return sorted(classes, key=lambda c: c.__module__.split('.')[-1])