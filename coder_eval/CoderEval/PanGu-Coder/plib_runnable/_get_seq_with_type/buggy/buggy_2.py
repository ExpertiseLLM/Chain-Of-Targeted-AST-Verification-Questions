def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, Sequence):
        return (seq, SequenceType.SEQUENCE)
    elif isinstance(seq, SequenceType):
        return (seq, SequenceType.SEQUENCE_TYPE)
    else:
        return (seq, SequenceType.SEQUENCE_TYPE)
