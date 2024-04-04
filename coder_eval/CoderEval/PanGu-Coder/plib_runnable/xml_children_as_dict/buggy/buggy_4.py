def xml_children_as_dict(node):
    result = {}
    for child in node.getchildren():
        tag = child.tag
        if tag in result:
            raise ValueError("Duplicate tag name %s" % tag)
        result[tag] = xml_children_as_dict(child)
    return result
