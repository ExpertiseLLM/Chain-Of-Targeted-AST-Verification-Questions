def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, (str, bytes)):
        return seq, None
    if isinstance(seq, Sequence):
        return seq, seq.__class__
    if bufsize is None:
        bufsize = sys.getsizeof(seq)
    return seq, seq.__class__((seq, Sequence(bufsize)))
