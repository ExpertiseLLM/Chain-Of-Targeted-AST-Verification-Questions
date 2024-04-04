def find_roots(
    graph:
	"""
	Find the roots in some sort of transitive hierarchy.

find_roots(graph, rdflib.RDFS.subClassOf)
will return a set of all roots of the sub-class hierarchy

Assumes triple of the form (child, prop, parent), i.e. the direction of
RDFS.subClassOf or SKOS.broader
	"""
	def find_roots_triple(c: rdflib.URIRef, p: rdflib.URIRef, o: rdflib.URIRef) -> set[rdflib.URIRef]:
		"""
		Find all the roots of the sub-class hierarchy.
		"""
		r = find_roots_triple(c, p, o)
		r.add(c)
		return r
	
	def find_parents(graph:
	"""Find the parents of some triples."""
	def find_parents_triple(c: rdflib.URIRef, p: rdflib.URIRef) -> set[rdflib.URIRef]:
		"""
		Find all the parents of the triples.
		"""
		#