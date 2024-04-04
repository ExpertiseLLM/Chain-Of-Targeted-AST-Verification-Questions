import requests, tarfile
from pathlib import Path


<insert generated code here>


def test_get_repo_archive():
    """Check the correctness of get_repo_archive
    """
    test_cases = dict()
    try:
        test_cases['test1'] = get_repo_archive('https://files.pythonhosted.org/packages/bf/40/a1b1810a09e3e85567c17831fcc2fc8e48ad9a1d3b02e8be940c43b908a8/jsonlines-2.0.0.tar.gz',
                            Path('/tmp/jsonlines-2.0.0.tar.gz')) == Path('/tmp/jsonlines-2.0.0')

    except Exception as error:
        test_cases['test1'] = type(error).__name__

    print(test_cases)

if __name__ == "__main__":
    test_get_repo_archive()
