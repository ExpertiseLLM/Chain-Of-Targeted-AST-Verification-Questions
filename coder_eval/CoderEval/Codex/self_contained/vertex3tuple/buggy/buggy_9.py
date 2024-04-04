def vertex3tuple(vertices):
	vertices = list(vertices)
	if len(vertices) == 1:
		return (vertices[0], vertices[0], vertices[0])
	elif len(vertices) == 2:
		return (vertices[0], vertices[0], vertices[1]), (vertices[1], vertices[1], vertices[0])
	else:
		last = vertices[-1]
		first = vertices[0]
		return tuple((last, vertices[i], vertices[i+1]) for i in range(len(vertices) - 1))

