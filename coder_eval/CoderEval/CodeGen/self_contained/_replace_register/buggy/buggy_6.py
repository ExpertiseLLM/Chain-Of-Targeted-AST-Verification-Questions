def _replace_register(flow_params, register_number, register_value):
	"""
	Replace value from flows to given register number

'register_value' key in dictionary will be replaced by register number
given by'register_number'

:param flow_params: Dictionary containing defined flows
:param register_number: The number of register where value will be stored
:param register_value: Key to be replaced by register number
	"""
	if'registers' in flow_params:
		for register in flow_params['registers']:
			if register['register_number'] == register_number:
				flow_params['registers'][register_number]['value'] = register_value
				return
	raise ValueError('Register number \'{0}\' not found in flow_params'.format(register_number))