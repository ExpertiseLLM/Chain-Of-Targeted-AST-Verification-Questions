def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if name[:2] == '"':
		name = name[2:-1]
	elif name[:1] == '"' and name[-1:] == '"':
		name = name[1:-1]
	return name

class Command(object):
	"""
	Base class for commands.
	"""
	def __init__(self, name, help):
		self.name = name
		self.help = help
		self.aliases = []
		self.hidden = False
		self.options = []
		self.short_help = ''
		self.long_help = ''
		self.hidden_option = ''
		self.required = False
		self.required_help = ''
		self.arguments = []
		self.boolean_options = []
		self.action = None
		self.aliases_dict = {}
		self.aliases_dict_raw = {}
		self.aliases_dict_raw_exclude = {}
		self.aliases_dict_exclude = {}
		self.aliases_dict_exclude = {}
		self.default_action_callable = None
		self.default_action_callable_args = None
		self.default_action_callable_kwargs = None
		self.default_action_callable_option = None
		self.default_action_callable_option_args = None
		self.default_action_callable_option_kwargs = None
		self.default_action_callable_option_required = False
		self.default_action_callable_option_required_help = ''
		self.default_action_callable_option_required_required = False
		self.default_action_callable_option_required_required_help = ''
		self.default_action_callable_option_required_required_default = False
		self.default_action_callable_option_required_required_required = False
		self.default_action_callable_option_required_required_default = False
		self.default_action_callable_option_required_required_required_default = False
		self.default_action_callable_option_required_required_required_default = False
		self.default_action_callable_option_required_required_required_default = False
		self.default_action_callable_option_required_required_required_default = False
		self.required_action = None
		self.required_action_callable = None
		self.required_action_callable_args = None
		self.required_action_callable_kwargs = None
		self.required_action_callable_option = None
		self.required_action_callable_option_args = None
		self.required_action_callable_option_kwargs = None
		self.required_action_callable_option_required = False
		self.required_action_callable_option_required_help = ''
		self.required_action_callable_option_required_required = False
		self.required_action_callable_option_required_required_help = ''
		self.required_action_callable_option_required_required_default = False
		self.required_action_callable_option_required_required_required = False
		self.required_action_callable_option_required_required_required_default = False
		self.required_action_callable_option_required_required_required_default = False
		self.required_action_callable_option_required_required_required_default = False
		self.required_action_callable_option_required_required_required_default = False
		self.required_action_callable_option_required_required_required_default = False
		self.required_action_callable_option_required_required_required_required_default = False
		self.required_action_callable_option_required_required_required_required_default = False
		self.required_action_callable_option_required_required_required_required_default = False
		self.required_action_callable_option_required_required_required_required_default = False
		self.required_action_callable_option_required_required_required_required_default