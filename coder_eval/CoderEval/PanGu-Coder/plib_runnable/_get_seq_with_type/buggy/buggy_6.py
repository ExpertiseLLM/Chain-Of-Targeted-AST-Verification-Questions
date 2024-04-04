def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, (six.string_types, six.binary_type)):
        return (seq, seq.dtype)
    if isinstance(seq, six.integer_types):
        return (seq, seq.dtype)
    if bufsize is None:
        bufsize = sys.getsizeof(seq)
    return (seq, np.dtype(seq.dtype))
