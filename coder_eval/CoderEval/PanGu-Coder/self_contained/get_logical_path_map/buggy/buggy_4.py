def get_logical_path_map(inventory, version):
    return _get_path_map(inventory, version, lambda x: x['logical_path'])
