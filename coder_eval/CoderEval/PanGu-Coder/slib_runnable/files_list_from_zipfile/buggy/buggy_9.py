def files_list_from_zipfile(zip_path):
    return [f for f in os.listdir(zip_path) if is_file_in_zip(f)]
