def paging(response, max_results):
	if len(response) > max_results:
		for page in range(0, len(response), max_results):
			yield response[page:page + max_results]
	else:
		yield response


