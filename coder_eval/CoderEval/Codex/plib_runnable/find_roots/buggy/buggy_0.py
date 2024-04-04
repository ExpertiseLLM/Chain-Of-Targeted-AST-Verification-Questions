def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
	roots = set() if roots is None else roots
	graph.addNodes(roots)
	for child in graph.transitive_closure_of(prop):
		if not graph.has_predicate((child, prop)):
			roots.add(child)
	return roots


