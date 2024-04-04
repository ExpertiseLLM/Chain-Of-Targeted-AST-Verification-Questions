def match_pubdate(node, pubdate_xpaths):
    
    
    for pubdate_xpath in pubdate_xpaths:
        pubdate_node = node.xpath(pubdate_xpath)
        if pubdate_node:
            return pubdate_node[0]
    return None
