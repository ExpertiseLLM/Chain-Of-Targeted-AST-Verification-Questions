def paging(response, max_results):
	offset = 0
	while True:
		response_page = response[offset:offset + max_results]
		if not response_page:
			break
		yield response_page
		offset += max_results

