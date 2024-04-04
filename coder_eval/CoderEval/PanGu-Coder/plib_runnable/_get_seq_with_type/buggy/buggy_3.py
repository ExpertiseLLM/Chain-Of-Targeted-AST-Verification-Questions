def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, Sequence):
        return seq, seq.__class__
    return seq, type(seq)
