def find_roots(
    graph:
	"""
	Find the roots in some sort of transitive hierarchy.

find_roots(graph, rdflib.RDFS.subClassOf)
will return a set of all roots of the sub-class hierarchy

Assumes triple of the form (child, prop, parent), i.e. the direction of
RDFS.subClassOf or SKOS.broader
	"""
	return set(rdflib.RDFS.objects(graph, rdflib.RDFS.subClassOf))

