def is_fill_request_el(obj):
    return (isinstance(obj, Element) and
            obj.tag == qn('svg:fill') and
            obj.attrib.get(qn('stroke')) == '#000000')
