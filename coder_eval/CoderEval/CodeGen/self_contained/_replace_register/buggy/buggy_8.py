def _replace_register(flow_params, register_number, register_value):
	"""
	Replace value from flows to given register number

'register_value' key in dictionary will be replaced by register number
given by'register_number'

:param flow_params: Dictionary containing defined flows
:param register_number: The number of register where value will be stored
:param register_value: Key to be replaced by register number
	"""
	param_dict = flow_params['param_dict']
	flow_params['param_dict'][register_number]['value'] = register_value
	flow_params['param_dict'][register_number]['flow_params'].pop(0)
	flow_params['param_dict'][register_number]['flow_params'].append(register_value)

