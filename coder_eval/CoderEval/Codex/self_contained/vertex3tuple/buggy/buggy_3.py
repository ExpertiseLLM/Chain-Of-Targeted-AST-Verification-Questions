def vertex3tuple(vertices):
	vertices_3tuple = []
	for i in range(len(vertices)):
		vertices_3tuple.append(vertices[i-1] + vertices[i] + vertices[(i+1) % len(vertices)])
	return vertices_3tuple

