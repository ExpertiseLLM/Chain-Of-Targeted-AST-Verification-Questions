def paging(response, max_results):
	if max_results is None or max_results > 500:
		max_results = 500
	if 'meta' not in response:
		yield response
	else:
		total_count = response['meta']['total_count']
		if total_count <= max_results:
			yield response
		else:
			for offset in range(0, total_count, max_results):
				for res in response['objects']:
					yield res
				response = wapi_get('/wapi/v2.7.1/' + response['_ref'].split('/')[-1],
				                    params={'_paging': '1', '_return_as_object': '1',
				                            '_max_results': str(max_results), '_return_fields+': '',
				                            '_offset': str(offset + max_results)})
				if '_ref' not in response or response['_ref']
