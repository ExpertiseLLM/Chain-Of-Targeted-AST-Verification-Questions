def get_logical_path_map(inventory, version):
    return {
        path
        for path in inventory.get_logical_paths(version)
        if path not in inventory.get_duplicate_paths(version)
    }
