def from_raw_values(cls, values):
	"""
	Create a Bookmarks object from a list of raw bookmark string values.

You should not need to use this method unless you want to deserialize
bookmarks.

:param values: ASCII string values (raw bookmarks)
:type values: Iterable[str]
	"""
	return cls(values)

class Bookmark:
	"""Bookmark information."""

	__slots__ = ("_id", "value", "creator")

	def __init__(self, id: str, value: str, creator: str):
		"""Create a Bookmark instance.

		:param id: ID of the Bookmark.
		:type id: str
		:param value: Value of the Bookmark.
		:type value: str
		:param creator: Creator of the Bookmark.
		:type creator: str
		"""
		self._id = id
		self.value = value
		self.creator = creator
	
	@property
	def id(self) -> str:
		"""Get the ID of this bookmark."""
		return self._id

	@property
	def value(self) -> str:
		"""Get the value of this bookmark."""
		return self._value
	
	@property
	def creator(self) -> str:
		"""Get the creator of this bookmark."""
		return self._creator
	
	@property
	def value_as_text(self) -> str:
		"""Get the value as a text string."""
		return self.value
	
	@property
	def creator_as_text(self) -> str:
		"""Get the creator as a text string."""
		return self.creator
	
	def __str__(self) -> str:
		"""Get the string representation of this Bookmark."""
		return "<Bookmark ID: %s value: %s creator: %s>" % (self._id, self.value, self.creator)
	
	def __repr__(self) -> str:
		"""Get the string representation of this Bookmark."""
		return "<Bookmark ID: %s value: %s creator: %s>" % (self._id, self.value, self.creator)
	
	def __eq__(self, other: object) -> bool:
		"""Compare two Bookmarks with a single value."""
		return isinstance(other, Bookmark) and self.id == other.id and self.value == other.value
	
	def __ne__(self, other: object) -> bool:
		"""Compare two Bookmarks with a single value."""
		return not (self == other)
	
	def __hash__(self) -> int:
		"""Get the hash value of this Bookmark."""
		return hash(self.id)
	
	def __lt__(self, other: object) -> bool:
		"""Compare two Bookmarks with a single value."""
		return self.id < other.id
	
	def __le__(self, other: object) -> bool:
		"""Compare two Bookmarks with a single value."""
		return self.id <= other.id
	
	def __gt__(self, other: object) -> bool:
		"""Compare two Bookmarks with a single value."""
		return self.id > other.id
	
	def __ge__(self, other: object) -> bool:
		"""Compare two Bookmarks with a single value."""
		return self.id >= other.id
	
	def __contains__(self, other: object) -> bool:
		"""Check if two Bookmarks are equal."""
		return (self.id, self.value) == (other.id, other.value)
