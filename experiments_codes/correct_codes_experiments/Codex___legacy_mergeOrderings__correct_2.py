def _legacy_mergeOrderings(orderings):
	if not orderings:
		return []
	# We don't want to modify the input, so make a copy
	orderings = [ordering[:] for ordering in orderings]
	# Remove redundant orderings
	orderings.sort(key=len)
	for ordering in orderings:
		for other in orderings:
			if ordering == other:
				continue
			if set(ordering).issubset(set(other)):
				ordering.clear()
	# Remove empty orderings
	orderings = [ordering for ordering in orderings if ordering]
	# Now append each ordering to the end of the current ordering
	pos = 0
	while orderings:
		# Find the ordering with the highest position
		highest = None
		for ordering in orderings:
			if highest is None or ordering[0] > highest:
				highest = ordering[0]
		# Remove the next element from each ordering
		for ordering in orderings:
			if ordering[0] != highest:
				ordering
