def vertex3tuple(vertices):
	v=[]
	for i in range(len(vertices)):
		v.append([vertices[i-2], vertices[i-1], vertices[i]])
	return v

