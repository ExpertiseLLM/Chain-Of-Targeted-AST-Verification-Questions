# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import oracle as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "j0 (#G?{BY"
    module_0.size_to_bytes(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "]?*3:[_y3ny`\rDHI0ni"
    module_0.size_to_bytes(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.size_to_bytes(bool_0)
