def is_fill_compute_el(obj):
	"""
	Object contains executable methods 'fill' and 'compute'.
	"""
	return (isinstance(obj, FillCompute) or
			isinstance(obj, Compute) or
			isinstance(obj, Fill) or
			isinstance(obj, Compute) or
			isinstance(obj, ComputeCompute) or
			isinstance(obj, ComputeFill) or
			isinstance(obj, ComputeFillCompute) or
			isinstance(obj, ComputeFillComputeFill) or
			isinstance(obj, ComputeFillComputeFillCompute) or
			isinstance(obj, ComputeFillComputeFillFill) or
			isinstance(obj, ComputeFillFillFillCompute) or
			isinstance(obj, ComputeFillFillFillFillCompute) or
			isinstance(obj, ComputeFillFillFillFillFillCompute) or
			isinstance(obj, ComputeFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillComputeFill) or
			isinstance(obj, ComputeFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFillFill