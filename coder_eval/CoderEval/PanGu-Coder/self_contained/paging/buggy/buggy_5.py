def paging(response, max_results):
    while len(response) > max_results:
        response = response[:max_results]
        yield response
