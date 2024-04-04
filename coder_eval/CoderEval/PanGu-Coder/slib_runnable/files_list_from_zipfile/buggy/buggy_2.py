def files_list_from_zipfile(zip_path):
    return [f for f in zip_path.iterdir() if f.is_file()]
