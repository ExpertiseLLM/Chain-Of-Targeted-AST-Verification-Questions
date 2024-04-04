def paging(response, max_results):
	"""
	Returns WAPI response page by page

Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
Returns:
    Generator object with WAPI response split page by page.
	"""
	while True:
		yield response
		page_token = response.meta['next_page_token']
		if page_token is None:
			break
		#