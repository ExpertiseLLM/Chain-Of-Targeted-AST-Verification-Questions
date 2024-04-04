def paging(response, max_results):
	max_pages = math.ceil(response[0]["total_count"]/max_results)
	print("Total pages: {}".format(max_pages))
	for page_num in range(0, max_pages):
		print("Page: {}".format(page_num))
		response = fw.get(
			"record:a",
			{"_paging": "1", "_return_as_object": "1", "max_results": max_results, "offset": page_num*max_results}
		)
		yield response

