def _dump_string(obj, dumper=None):
	# TODO: Remove this method in the future.
	# I might have to keep it if I want to be able to dump to a string
	# with py2
	return _dump(obj, dumper=dumper, fp=io.StringIO()).getvalue()


