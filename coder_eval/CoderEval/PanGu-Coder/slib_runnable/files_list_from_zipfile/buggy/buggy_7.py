def files_list_from_zipfile(zip_path):
    files_list = [f for f in os.listdir(zip_path) if is_file_in_zip(zip_path, f)]
    return files_list
