def vertex3tuple(vertices):
	assert len(vertices)>=3
	v1 = vertices[:-2]
	v2 = vertices[1:-1]
	v3 = vertices[2:]
	return zip(v1, v2, v3)

