def paging(response, max_results):
	while len(response) > 0:
		response = infoblox.paging(response, max_results)
		yield response


