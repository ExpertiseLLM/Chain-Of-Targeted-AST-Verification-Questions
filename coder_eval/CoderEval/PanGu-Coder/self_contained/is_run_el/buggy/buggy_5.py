def is_run_el(obj):
    return isinstance(obj, (MethodType, FunctionType)) and obj.__name__ == 'run'