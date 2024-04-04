"""Check whether a sequence can be converted to a Lena Sequence."""
# otherwise import errors arise
# from . import source
import sys
sys.path.append("/home/travis/builds/repos/ynikitenko---lena/")
def is_fill_compute_el(obj):
    """Object contains executable methods 'fill' and 'compute'."""
    return (hasattr(obj, "fill")
            and hasattr(obj, "compute")
            and callable(obj.fill)
            and callable(obj.compute))


def is_fill_compute_seq(seq):
    """Test whether *seq* can be converted to a FillComputeSeq.

    True only if it is a FillCompute element
    or contains at least one such,
    and it is not a Source sequence.
    """
    if is_source(seq):
        return False
    is_fcseq = False
    try:
        is_fcseq = any(map(is_fill_compute_el, seq))
    except TypeError:
        # seq is non-iterable
        pass
    if is_fill_compute_el(seq):
        is_fcseq = True
    return is_fcseq


<insert generated code here>


def is_fill_request_seq(seq):
    """Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    if is_source(seq):
        return False
    is_fcseq = False
    if hasattr(seq, "__iter__"):
        is_fcseq = any(map(is_fill_request_el, seq))
    if is_fill_request_el(seq):
        is_fcseq = True
    return is_fcseq


def is_run_el(obj):
    """Object contains executable method 'run'."""
    return hasattr(obj, "run") and callable(obj.run)


def is_source(seq):
    """Sequence is a Source, if and only if its type is Source."""
    # Otherwise lambdas would be counted as Source,
    # but they must be converted to Sequences.
    # Moreover: this makes Source elements explicit and visible in code.
    from . import source
    return isinstance(seq, source.Source)

if __name__ == "__main__":
    isT = True
    from lena.math.elements import Sum, DSum, Mean
    from lena.core.source import Source
    from lena.flow import CountFrom
    test_cases = dict()
    try:
        res1 = is_fill_compute_el(Sum())
        test_cases['test1'] = res1
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = is_fill_compute_el(DSum())
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:
        res3 = is_fill_compute_el(Mean())
        test_cases ['test3'] = res3
    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:
        test_cases['test4'] = is_fill_compute_el(Source(CountFrom()))
    except Exception as error:
        test_cases['test4'] = type(error).__name__
    print(test_cases)





