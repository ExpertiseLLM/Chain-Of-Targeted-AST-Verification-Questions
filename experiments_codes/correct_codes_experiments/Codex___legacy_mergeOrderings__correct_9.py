def _legacy_mergeOrderings(orderings):
	suffixes = []
	order = []
	for ordering in orderings:
		# find the suffixes that begin with each element of the ordering
		suffixes = []
		for element in ordering:
			suffixes.extend([s for s in suffixes if s[0] == element])
			suffixes.append([element])
		# if it's a new element, add it to the order
		for suffix in suffixes:
			for element in suffix:
				if element not in order:
					order.append(element)
	return order

