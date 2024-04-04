def vertex3tuple(vertices):
    return tuple(map(tuple, zip(vertices[0::3], vertices[1::3], vertices[2::3])))
