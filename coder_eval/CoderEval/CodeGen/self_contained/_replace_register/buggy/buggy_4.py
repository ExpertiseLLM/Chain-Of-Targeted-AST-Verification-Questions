def _replace_register(flow_params, register_number, register_value):
	"""
	Replace value from flows to given register number

'register_value' key in dictionary will be replaced by register number
given by'register_number'

:param flow_params: Dictionary containing defined flows
:param register_number: The number of register where value will be stored
:param register_value: Key to be replaced by register number
	"""
	flow_params_copy = flow_params.copy()
	if register_number not in flow_params_copy:
		flow_params[register_number] = register_value
	else:
		if register_value in flow_params_copy:
			flow_params[register_number] = register_value

