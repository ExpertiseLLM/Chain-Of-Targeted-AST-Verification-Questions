def paging(response, max_results):
	if max_results > 0:
		for i in range(0, len(response), max_results):
			yield response[i:i + max_results]
	else:
		yield response


