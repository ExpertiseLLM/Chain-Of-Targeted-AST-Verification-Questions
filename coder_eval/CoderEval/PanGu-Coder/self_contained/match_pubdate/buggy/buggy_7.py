def match_pubdate(node, pubdate_xpaths):
    
    
    for pubdate_xpath in pubdate_xpaths:
        match = node.xpath(pubdate_xpath)
        if match:
            return match[0]
    return None
