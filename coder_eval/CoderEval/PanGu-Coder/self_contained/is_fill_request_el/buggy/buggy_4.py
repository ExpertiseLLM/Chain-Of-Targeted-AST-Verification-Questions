def is_fill_request_el(obj):
    return isinstance(obj, (ExecutableMethod, SequenceMethod, SetMethod))
