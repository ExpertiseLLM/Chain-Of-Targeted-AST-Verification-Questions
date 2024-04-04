def _legacy_mergeOrderings(orderings):
	# We use a set to represent the ordering, since we don't care
	# about duplicates.
	ordering = set()
	for o in orderings:
		ordering = set(o).union(ordering)
	return list(ordering)

