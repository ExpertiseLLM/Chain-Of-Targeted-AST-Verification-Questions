def vertex3tuple(vertices):
    return tuple((vertices[i], vertices[i+1], vertices[i+2]) for i in range(len(vertices)-1))