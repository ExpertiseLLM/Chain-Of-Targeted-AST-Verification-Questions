def find_roots(
    graph:
	"""
	Find the roots in some sort of transitive hierarchy.

find_roots(graph, rdflib.RDFS.subClassOf)
will return a set of all roots of the sub-class hierarchy

Assumes triple of the form (child, prop, parent), i.e. the direction of
RDFS.subClassOf or SKOS.broader
	"""
	root_set = set()
	for n in graph.objects(graph.RDFS.subClassOf):
		for c in graph.objects(n, graph.RDFS.subClassOf):
			for prop in graph.objects(c, graph.RDFS.subClassOf):
				root_set.add(prop)
	for n in graph.objects(graph.RDFS.subClassOf):
		root_set.update(graph.objects(n, graph.RDFS.subClassOf))
	for p in graph.objects(graph.RDFS.subClassOf):
		for c in graph.objects(p, graph.RDFS.subClassOf):
			root_set.add(c)
	return root_set

