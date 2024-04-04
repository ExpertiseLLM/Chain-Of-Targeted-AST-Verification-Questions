def get_logical_path_map(inventory, version):
    return {
        p: set(
            content_files
            for content_files in inventory[p]
            if content_files.version == version
        )
    }
