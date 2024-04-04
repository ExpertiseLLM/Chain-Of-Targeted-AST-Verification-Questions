def _c_optimizations_ignored():
	return (
		not _c_optimizations_required()
		and not _c_optimizations_desired()
	)

