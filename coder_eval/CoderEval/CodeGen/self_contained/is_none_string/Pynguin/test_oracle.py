# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import builtins as module_0
import oracle as module_1


def test_case_0():
    object_0 = module_0.object()
    bool_0 = module_1.is_none_string(object_0)
    assert bool_0 is False
    str_0 = "0zig(wme[3g1Ju.F2mx"
    bool_1 = module_1.is_none_string(str_0)
    assert bool_1 is False
    bool_2 = module_1.is_none_string(bool_1)
    assert bool_2 is False


def test_case_1():
    none_type_0 = None
    bool_0 = module_1.is_none_string(none_type_0)
    assert bool_0 is False
    bool_1 = module_1.is_none_string(none_type_0)
    assert bool_1 is False
    bool_2 = module_1.is_none_string(none_type_0)
    assert bool_2 is False
