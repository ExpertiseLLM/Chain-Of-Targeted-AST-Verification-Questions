# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xebIp\x1fw\xb0M\xb3g\xf1E\x80\x8a~p\x14\x99\n"
    module_0.get(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "u Q"
    tuple_0 = (str_0, str_0)
    var_0 = module_0.get(tuple_0, tuple_0)
    complex_0 = 2406 + 823.011658j
    module_0.get(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.get(none_type_0)
