import logging
import os
import sys
sys.path.append("/home/travis/builds/repos/scieloorg---packtools/")
from packtools import file_utils
from zipfile import ZipFile


logger = logging.getLogger(__name__)


class Package:
    def __init__(self, source, name):
        self._source = source
        self._xml = None
        self._assets = {}
        self._renditions = {}
        self._name = name
        self.zip_file_path = file_utils.is_zipfile(source) and source

    @property
    def assets(self):
        return self._assets

    @property
    def name(self):
        return self._name

    def file_path(self, file_path):
        if file_utils.is_folder(self._source):
            return os.path.join(self._source, file_path)
        return file_path

    def add_asset(self, basename, file_path):
        """
        "{
            "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
            "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
            "artigo02-gf03.png": "/path/artigo02-gf03.png",
        }
        """
        self._assets[basename] = self.file_path(file_path)

    def get_asset(self, basename):
        try:
            return self._assets[basename]
        except KeyError:
            return

    def add_rendition(self, lang, file_path):
        """
        {
            "original": "artigo02.pdf",
            "en": "artigo02-en.pdf",
        }
        """
        self._renditions[lang] = self.file_path(file_path)

    def get_rendition(self, lang):
        try:
            return self._renditions[lang]
        except KeyError:
            return

    @property
    def source(self):
        return self._source

    @property
    def xml(self):
        return self.file_path(self._xml)

    @xml.setter
    def xml(self, value):
        self._xml = value

    @property
    def renditions(self):
        return self._renditions

    @property
    def xml_content(self):
        if file_utils.is_folder(self._source):
            with open(self.xml, "rb") as fp:
                return fp.read()
        with ZipFile(self._source) as zf:
            return zf.read(self.xml)


def select_filenames_by_prefix(prefix, files):
    """
    Get files which belongs to a document package.

    Retorna os arquivos da lista `files` cujos nomes iniciam com `prefix`

    Parameters
    ----------
    prefix : str
        Filename prefix
    files : str list
        Files paths
    Returns
    -------
    list
        files paths which basename files matches to prefix
    """
    return [
        item
        for item in files
        if match_file_by_prefix(prefix, item)
    ]


<insert generated code here>


def explore_source(source):
    packages = _explore_zipfile(source)
    if not packages:
        packages = _explore_folder(source)
    if not packages:
        raise ValueError("%s: Invalid value for `source`" % source)
    return packages


def _explore_folder(folder):
    """
    Get packages' data from folder

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    folder : str
        Folder of the package
    Returns
    -------
    dict
    """
    if file_utils.is_folder(folder):
        data = _group_files_by_xml_filename(
            folder,
            file_utils.xml_files_list(folder),
            file_utils.files_list(folder),
        )
        return data


def _explore_zipfile(zip_path):
    """
    Get packages' data from zip_path

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    zip_path : str
        zip file path
    Returns
    -------
    dict
    """
    if file_utils.is_zipfile(zip_path):
        with ZipFile(zip_path, 'r'):
            data = _group_files_by_xml_filename(
                zip_path,
                file_utils.xml_files_list_from_zipfile(zip_path),
                file_utils.files_list_from_zipfile(zip_path),
            )
            return data


def _group_files_by_xml_filename(source, xmls, files):
    """
    Group files by their XML basename

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    xml_filename : str
        XML filenames
    files : list
        list of files in the folder or zipfile

    Returns
    -------
    dict
        key: name of the XML files
        value: Package
    """
    docs = {}
    for xml in xmls:
        basename = os.path.basename(xml)
        prefix, ext = os.path.splitext(basename)

        docs.setdefault(prefix, Package(source, prefix))

        # XML
        docs[prefix].xml = xml

        for file in select_filenames_by_prefix(prefix, files):
            # avalia arquivo do pacote, se é asset ou rendition
            component = _eval_file(prefix, file)
            if not component:
                continue

            # resultado do avaliação do pacote
            ftype = component.get("ftype")
            file_path = component["file_path"]
            comp_id = component["component_id"]

            if ftype:
                docs[prefix].add_asset(comp_id, file_path)
            else:
                docs[prefix].add_rendition(comp_id, file_path)
            files.remove(file)
    return docs


def _eval_file(prefix, file_path):
    """
    Identifica o tipo de arquivo do pacote: `asset` ou `rendition`.

    Identifica o tipo de arquivo do pacote e atualiza `packages` com o tipo e
    o endereço do arquivo em análise.

    Parameters
    ----------
    prefix : str
        nome do arquivo XML sem extensão
    filename : str
        filename
    file_folder : str
        file folder

    Returns
    -------
    dict
    """
    if not match_file_by_prefix(prefix, file_path):
        # ignore files which name does not match
        return
    if file_path.endswith(".xml"):
        # ignore XML files
        return

    # it matches
    filename = os.path.basename(file_path)
    fname, ext = os.path.splitext(filename)

    lang = None
    if ext == ".pdf":
        suffix = fname.replace(prefix, "")
        if fname == prefix:
            lang = "original"
        elif len(suffix) == 3 and suffix[0] == "-":
            # it is a rendition
            lang = suffix[1:]

    if lang:
        return dict(
            component_id=lang,
            file_path=file_path,
        )
    else:
        return dict(
            component_id=filename,
            component_name=fname,
            ftype=ext[1:],
            file_path=file_path,
        )


if __name__ == "__main__":
    isT=True
    pkg1 = Package("source", "name")
    pkg11 = Package("source", "name")

    pkg11.xml = "a11.xml"
    pkg11._assets = {
        "a11-gf01-es.tiff": "a11-gf01-es.tiff",
        "a11-gf02-es.tiff": "a11-gf02-es.tiff",
        "a11-suppl-es.pdf": "a11-suppl-es.pdf",
    }
    pkg11._renditions = {
        "es": "a11-es.pdf",
        "original": "a11.pdf",
    }

    pkg1.xml = "a1.xml"
    pkg1._assets = {
        "a1-gf01.tiff": "a1-gf01.tiff",
        "a1-gf01.jpg": "a1-gf01.jpg",
        "a1-gf02.tiff": "a1-gf02.tiff",
    }
    pkg1._renditions = {
        "en": "a1-en.pdf",
        "original": "a1.pdf",
    }
    xmls = [
        "a1.xml", "a11.xml",
    ]
    files = [
        "a1-en.pdf",
        "a1-gf01.jpg",
        "a1-gf01.tiff",
        "a1-gf02.tiff",
        "a1.pdf",
        "a1.xml",
        "a11-es.pdf",
        "a11-gf01-es.tiff",
        "a11-gf02-es.tiff",
        "a11-suppl-es.pdf",
        "a11.pdf",
        "a11.xml",
    ]
    test_cases = dict()
    try:
        result = _group_files_by_xml_filename("source", xmls, files)
    except Exception as error:
        test_cases['test'] = type(error).__name__
        print(test_cases)
    ist1=pkg11.xml== result["a11"].xml
    ist2=pkg11._assets==result["a11"]._assets
    ist3=pkg11._renditions== result["a11"]._renditions
    ist4=pkg1.xml== result["a1"].xml
    ist5=pkg1._assets== result["a1"]._assets
    ist6=pkg1._renditions== result["a1"]._renditions
    numberOfTestCases = 0
    numberOfTestCases += ist1 + ist2 + ist3 + ist4 + ist5 + ist6
    test_cases['test_cases'] = numberOfTestCases
    print(test_cases)




