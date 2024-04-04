def from_raw_values(cls, values):
	"""
	Create a Bookmarks object from a list of raw bookmark string values.

You should not need to use this method unless you want to deserialize
bookmarks.

:param values: ASCII string values (raw bookmarks)
:type values: Iterable[str]
	"""
	return cls(
		name=values[0],
		path=values[1],
		title=values[2],
		author=values[3],
		publisher=values[4],
		status=values[5],
		notes=values[6],
	)

class Bookmark:
	"""
	A Bookmark object.
	"""

	def __init__(self, name, path, title, author, publisher, status, notes):
		self.name = name
		self.path = path
		self.title = title
		self.author = author
		self.publisher = publisher
		self.status = status
		self.notes = notes

	def __repr__(self):
		return 'Bookmark(name="{}", path="{}", title="{}", author="{}", publisher="{}", status="{}", notes="{}")'.format(self.name, self.path, self.title, self.author, self.publisher, self.status, self.notes)

	def __str__(self):
		return 'Bookmark(name="{}", path="{}", title="{}", author="{}", publisher="{}", status="{}", notes="{}")'.format(self.name, self.path, self.title, self.author, self.publisher, self.status, self.notes)

	def __eq__(self, other):
		if isinstance(other, Bookmark):
			return self.name == other.name and self.path == other.path and self.title == other.title and self.author == other.author and self.publisher == other.publisher and self.status == other.status and self.notes == other.notes
		else:
			return NotImplemented

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.name) ^ hash(self.path) ^ hash(self.title) ^ hash(self.author) ^ hash(self.publisher) ^ hash(self.status) ^ hash(self.notes)

	def __lt__(self, other):
		return self.name < other.name or (self.name == other.name and self.path < other.path)

	def __le__(self, other):
		return self.name <= other.name or (self.name == other.name and self.path <= other.path)

	def __gt__(self, other):
		return self.name > other.name or (self.name == other.name and self.path > other.path)

	def __ge__(self, other):
		return self.name >= other.name or (self.name == other.name and self.path >= other.path)

	def __bool__(self):
		return self.name!= self.title

	@property
	def is_dir(self):
		"""
		Returns True if the bookmark is a directory.
		"""
		return self.path.startswith('/')

	@property
	def is_file(self):
		"""
		Returns True if the bookmark is a file.
		"""
		return self.path.startswith('/') and not self.path.endswith('/')

	def get_path(self):
		return self.path

	def get_path_prefixed(self):
		return self.path[1:] if self.is_dir else self.path

	def get_path_with_name(self):
		return self.path + '/' + self.name

	def get_path_with_title(self):
		return '/'.join(self.path.split('/')[:self.path.index('/')]) + '/' + self.title

	def get_path_with_author(self):
		return '/'.join(self.path.split('/')[:self.path.index('/')]) + '/' + self.author

	def get_path