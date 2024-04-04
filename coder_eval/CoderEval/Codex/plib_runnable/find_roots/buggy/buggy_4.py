def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
	if roots is None:
		roots = set()
	for child, parent in graph.subject_objects(prop):
		if child in roots:
			continue
		roots.add(child)
		find_roots(graph, prop, roots)
	return roots


