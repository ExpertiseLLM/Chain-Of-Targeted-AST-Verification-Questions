def get_logical_path_map(inventory, version):

    """Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described."""
    return {
        path_in_state(inventory, content_file): content_files
        for content_files in get_content_files_in_state(inventory, version)
    }
