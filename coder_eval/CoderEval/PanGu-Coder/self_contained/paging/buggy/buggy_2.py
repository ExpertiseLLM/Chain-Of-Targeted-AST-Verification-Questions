def paging(response, max_results):
    page = 0
    while page <= max_results:
        yield response[page]
        page += 1
