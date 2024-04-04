def _legacy_mergeOrderings(orderings):
	if len(orderings) == 0:
		return []
	if len(orderings) == 1:
		return orderings[0]
	orderings = [list(o) for o in orderings]
	head, tail = orderings[0], orderings[1:]
	for ordering in tail:
		for i, value in enumerate(ordering):
			if value in head:
				ordering = ordering[i:]
				break
		else:
			raise ValueError("Incompatible orderings")
		head = [v for v in head if v in ordering] + ordering
	return head


