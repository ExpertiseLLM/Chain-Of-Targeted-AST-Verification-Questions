def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
	if roots is None:
		roots = set()
	else:
		roots = set(roots)
	for (child, parent) in graph.subject_objects(prop):
		if child not in roots:
			roots.add(parent)
			find_roots(graph, prop, roots)
	return roots


