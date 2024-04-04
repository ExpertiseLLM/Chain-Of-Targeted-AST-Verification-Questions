def vertex3tuple(vertices):
    pts = []
    for i in range(len(vertices) - 1):
        pts.append(vertices[i])
        pts.append(vertices[i + 1])
    return tuple(pts)
