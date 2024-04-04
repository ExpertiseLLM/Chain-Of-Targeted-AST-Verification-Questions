def paging(response, max_results):
    for page in range(1, max_results + 1):
        for item in response:
            yield item
        if page == max_results:
            break
