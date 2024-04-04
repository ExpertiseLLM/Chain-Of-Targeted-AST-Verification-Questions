def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, seq_types):
        return (seq, seq_types[seq.__class__])
    if isinstance(seq, (list, tuple)):
        return seq
    if isinstance(seq, dict):
        return seq_types[type(seq)](seq)
    raise TypeError("Cannot determine sequence type from sequence of type {}".format(type(seq)))
