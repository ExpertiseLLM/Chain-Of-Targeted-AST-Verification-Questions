def _legacy_mergeOrderings(orderings):
	orderings = [tuple(ordering) for ordering in orderings]
	# sort orderings by length
	orderings.sort(key=len)

	# merge orderings
	merged = []
	seen = set()
	while orderings:
		# first, get the next ordering
		ordering = orderings.pop(0)
		# if we've already seen the first item in this ordering, we're done
		if ordering[0] in seen:
			continue
		# otherwise, add the suffix that starts with this item to the result
		suffix = [ordering[0]]
		for item in ordering[1:]:
			suffix.append(item)
			seen.add(item)
		merged.extend(suffix)

	return merged


