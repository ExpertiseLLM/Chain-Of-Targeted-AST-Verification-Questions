def paging(response, max_results):

    page = 1
    while page <= max_results:
        for result in response[page - 1]:
            yield result
        page += 1
