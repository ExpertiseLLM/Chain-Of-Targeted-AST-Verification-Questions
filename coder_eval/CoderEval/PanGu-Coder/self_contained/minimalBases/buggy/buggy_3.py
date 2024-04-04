def minimalBases(classes):
    minimal = []
    for classe in classes:
        if classe.__bases__:
            for base in classe.__bases__:
                if base not in minimal:
                    minimal.append(base)
    return minimal
