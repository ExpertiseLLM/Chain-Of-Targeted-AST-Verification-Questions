def find_roots(
    graph:
	"""
	Find the roots in some sort of transitive hierarchy.

find_roots(graph, rdflib.RDFS.subClassOf)
will return a set of all roots of the sub-class hierarchy

Assumes triple of the form (child, prop, parent), i.e. the direction of
RDFS.subClassOf or SKOS.broader
	"""
	class_ = graph.objects.get(rdflib.URIRef(graph.bind('rdfS')))
	if class_ is None:
		raise TypeError("No class exists for this graph")
	roots = set(graph.subjects(
		subjectClass=class_,
		subjectProperty=rdflib.URIRef("$class")
		))
	return roots

