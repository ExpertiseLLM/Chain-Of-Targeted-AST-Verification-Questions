def files_list_from_zipfile(zip_path):
    with zipfile.ZipFile(zip_path) as zip:
        return [f.filename for f in zip.filelist]
