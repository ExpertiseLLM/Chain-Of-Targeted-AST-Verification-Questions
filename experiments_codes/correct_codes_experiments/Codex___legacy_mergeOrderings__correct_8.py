def _legacy_mergeOrderings(orderings):
	# TODO: This is not correct for all test cases
	merged = []
	for ordering in orderings:
		for item in ordering:
			if item not in merged:
				merged.append(item)
	return merged

