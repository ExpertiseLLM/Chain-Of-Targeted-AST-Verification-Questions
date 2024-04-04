def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, (list, tuple)):
        return seq, seq.__class__
    elif isinstance(seq, dict):
        return list(seq.items()), seq.__class__
    else:
        return (seq, seq.__class__), seq.__class__
