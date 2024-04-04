def _get_seq_with_type(seq, bufsize=None):
    if not isinstance(seq, Sequence):
        seq = Sequence(seq, bufsize)

    return seq, type(seq)
