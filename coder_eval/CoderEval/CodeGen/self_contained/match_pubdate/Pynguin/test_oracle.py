# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0


def test_case_0():
    bytes_0 = b"S\xab\xbfv"
    var_0 = module_0.match_pubdate(bytes_0, bytes_0)
    assert var_0 == 0


def test_case_1():
    dict_0 = {}
    var_0 = module_0.match_pubdate(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.match_pubdate(none_type_0, none_type_0)
