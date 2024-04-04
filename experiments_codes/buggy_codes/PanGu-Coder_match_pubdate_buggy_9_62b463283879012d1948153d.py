def match_pubdate(node, pubdate_xpaths):

    """Returns the first match in the pubdate_xpaths list"""
    for pubdate_xpath in pubdate_xpaths:
        pubdate_el = node.xpath(pubdate_xpath)
        if pubdate_el:
            return pubdate_el[0].text
