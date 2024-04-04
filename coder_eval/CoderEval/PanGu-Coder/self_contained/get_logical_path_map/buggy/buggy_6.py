def get_logical_path_map(inventory, version):
    return dict((os.path.join(state, filename), set(content_files))
                for state, content_files in inventory.items()
                if os.path.join(state, filename) in inventory)
