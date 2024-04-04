def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, sequence):
        return (seq, seq.type)
    elif isinstance(seq, sequence_type):
        return (seq, seq.__class__)
    elif isinstance(seq, type):
        return (seq, type)
    else:
        raise TypeError("seq must be a sequence, sequence_type, or a type")
