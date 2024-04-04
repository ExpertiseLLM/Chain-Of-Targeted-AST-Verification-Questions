def _get_seq_with_type(seq, bufsize=None):
    """Return a (sequence, type) pair.
    Sequence is derived from *seq*
    (or is *seq*, if that is of a sequence type).
    """
    seq_type = ""
    if isinstance(seq, source.Source):
        seq_type = "source"
    elif isinstance(seq, fill_compute_seq.FillComputeSeq):
        seq_type = "fill_compute"
    elif isinstance(seq, fill_request_seq.FillRequestSeq):
        seq_type = "fill_request"
    elif isinstance(seq, sequence.Sequence):
        seq_type = "sequence"

    if seq_type:
        # append later
        pass
    ## If no explicit type is given, check seq's methods
    elif ct.is_fill_compute_seq(seq):
        seq_type = "fill_compute"
        if not ct.is_fill_compute_el(seq):
            seq = fill_compute_seq.FillComputeSeq(*seq)
    elif ct.is_fill_request_seq(seq):
        seq_type = "fill_request"
        if not ct.is_fill_request_el(seq):
            seq = fill_request_seq.FillRequestSeq(
                *seq, bufsize=bufsize,
                # if we have a FillRequest element inside,
                # it decides itself when to reset.
                reset=False,
                # todo: change the interface, because
                # no difference with buffer_output: we fill
                # without a buffer
                buffer_input=True
            )
    # Source is not checked,
    # because it must be Source explicitly.
    else:
        try:
            if isinstance(seq, tuple):
                seq = sequence.Sequence(*seq)
            else:
                seq = sequence.Sequence(seq)
        except exceptions.LenaTypeError:
            raise exceptions.LenaTypeError(
                "unknown argument type. Must be a "
                "FillComputeSeq, FillRequestSeq or Source, "
                "{} provided".format(seq)
            )
        else:
            seq_type = "sequence"
    return (seq, seq_type)
