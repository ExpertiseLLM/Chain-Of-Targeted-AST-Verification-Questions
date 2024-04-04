def paging(response, max_results):
    page = 1
    while page <= max_results:
        yield response[page * max_results:(page + 1) * max_results]
        page += 1
