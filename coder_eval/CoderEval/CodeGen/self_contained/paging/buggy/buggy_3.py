def paging(response, max_results):
	"""
	Returns WAPI response page by page

Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
Returns:
    Generator object with WAPI response split page by page.
	"""
	for response_item in response:
		yield response_item
		if response_item['next']:
			next_page_url = response_item['next']['url']
			yield from paging(response_item['next'], max_results)
			if next_page_url:
				yield from paging(requests.get(next_page_url).json(), max_results)import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

