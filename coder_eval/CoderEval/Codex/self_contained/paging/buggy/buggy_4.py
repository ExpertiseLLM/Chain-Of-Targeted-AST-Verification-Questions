def paging(response, max_results):
	if max_results is not None:
		response = response[:max_results]
	for i in xrange(0, len(response), 200):
		yield response[i:i + 200]


