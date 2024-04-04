def _reset_logging(cls):
	"""
	Reset
	"""
	logging.disable(logging.CRITICAL)

class Logger(object):
	"""
	:class:`Logger` is the base class for all loggers. It provides the following
	methods:

	* :meth:`info`
	* :meth:`debug`
	* :meth:`warning`
	* :meth:`error`
	* :meth:`critical`
	
	The following attributes are available:

	* :attr:`name`
	* :attr:`level`
	* :attr:`formatters`
	* :attr:`filter`
	* :attr:`datefmt`
	* :attr:`style`
	* :attr:`converter`
	* :attr:`formatter_config`
	* :attr:`filename`
	* :attr:`filemode`
	* :attr:`mode`
	* :attr:`encoding`
	* :attr:`errors`
	* :attr:`stream`
	* :attr:`terminator`
	* :attr:`logger_level`
	"""
	def __init__(self, name=None):
		self.name = name or id(self)
		self.logger_level = logging.INFO
		if hasattr(self, 'level'):
			self.logger_level = self.level
		self.formatters = _LoggerFormatter()
		self.filters = []
		self.datefmt = None
		self.style = None
		self.converter = None
		self.formatter_config = None
		self.filename = None
		self.filemode = 'w'
		self.mode = 'a'
		self.encoding = 'utf-8'
		self.errors ='replace'
		self.stream = None
		self.terminator = '\n'
		self.logger_level = logging.INFO
		self.logger_manager = None

	def set_formatter(self, formatter=None):
		"""
		Set formatter
		
		:param formatter: :class:`logging.Formatter` instance
		:return: None
		"""
		if formatter is None:
			formatter = logging.Formatter(fmt=self.formatters.default_fmt, datefmt=self.datefmt, style=self.style,
										  converter=self.converter,
										  filters=self.filters, datefmt=self.datefmt, style=self.style,
										  fmt=self.formatters.formatter_fmt,
										  encoding=self.encoding, errors=self.errors,
										  stream=self.stream,
										  level=self.logger_level)
		self.formatters = self.formatters.copy()
		self.formatters.update(formatter)

	def get_formatter(self):
		"""
		Get formatter
		
		:return: :class:`logging.Formatter` instance
		"""
		return self.formatters

	def set_logger_level(self, level):
		"""
		Set logger level
		
		:param level: :class:`logging.Level` instance
		:return: None
		"""
		self.logger_level = level
		self.logger_manager = get_logger(self.name)
		self.logger_manager.setLevel(self.logger_level)
		self.logger_manager.debug = self.debug
		self.logger_manager.info = self.info
		self.logger_manager.warning = self.warning
		self.logger_manager.error = self.error
		self.logger_manager.critical = self.critical
		self.logger_manager.debug = self.debug
		self.logger_manager.info = self.info
		self.logger_manager.warning = self.warning
		self.logger_manager.error = self.error
		self.logger_manager.critical = self.critical

	def set_filters(self, filters):
		"""
		Set filters