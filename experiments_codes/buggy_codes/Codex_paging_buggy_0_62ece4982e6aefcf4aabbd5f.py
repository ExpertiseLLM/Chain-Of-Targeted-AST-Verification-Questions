def paging(response, max_results):
    """Returns WAPI response page by page

Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
Returns:
    Generator object with WAPI response split page by page."""
    while True:
        for r in response:
            yield r
        if '_next_id' not in response._meta:
            break
        next_id = response._meta['_next_id']
        response = infoblox.get_object(object_type, return_fields=return_fields, max_results=max_results,
                                       _max_results=max_results, _return_fields=return_fields,
                                       _paging_identifier=next_id)
