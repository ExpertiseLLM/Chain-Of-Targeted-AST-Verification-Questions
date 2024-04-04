def from_raw_values(cls, values):
	"""
	Create a Bookmarks object from a list of raw bookmark string values.

You should not need to use this method unless you want to deserialize
bookmarks.

:param values: ASCII string values (raw bookmarks)
:type values: Iterable[str]
	"""
	return cls(values)

class Bookmarks(object):
	"""
	A list of Bookmarks objects.
	"""
	def __init__(self, values):
		"""
		Create a Bookmarks object from a list of raw bookmarks.
		
		:param values: A list of raw bookmarks
		:type values: Iterable[str]
		"""
		self.values = values
	
	def __repr__(self):
		"""
		Return a string representation of the Bookmarks object.
		
		:return: A string representation of the Bookmarks object
		:rtype: str
		"""
		return "<Bookmarks: %r>" % self.values
	
	def __eq__(self, other):
		"""
		Return ``True`` if the Bookmarks object is equivalent to another.
		
		:param other: Another Bookmarks object
		:type other: Bookmarks
		:return: ``True`` if the Bookmarks object is equivalent to another
		:rtype: bool
		"""
		return self.values == other.values
	
	def __ne__(self, other):
		"""
		Return ``False`` if the Bookmarks object is equivalent to another.
		
		:param other: Another Bookmarks object
		:type other: Bookmarks
		:return: ``False`` if the Bookmarks object is equivalent to another
		:rtype: bool
		"""
		return self.values!= other.values
	
	def __len__(self):
		"""
		Return the number of Bookmarks.
		
		:return: The number of Bookmarks
		:rtype: int
		"""
		return len(self.values)
	
	def __getitem__(self, key):
		"""
		Return the Bookmarks object associated with the given index.

		:param key: Index of the Bookmarks object to return
		:type key: int
		:return: The Bookmarks object associated with the given index
		:rtype: Bookmarks
		"""
		return self.values[key]
	
	def __add__(self, other):
		"""
		Return the Bookmarks object concatenated with another Bookmarks object.
		
		:param other: Another Bookmarks object
		:type other: Bookmarks
		:return: A Bookmarks object concatenated with another Bookmarks object
		:rtype: Bookmarks
		"""
		return Bookmarks(self.values + other.values)
	
	def __iadd__(self, other):
		"""
		Concatenate two Bookmarks objects.
		
		:param other: Another Bookmarks object
		:type other: Bookmarks
		:return: A Bookmarks object concatenated with another Bookmarks object
		:rtype: Bookmarks
		"""
		self.values += other.values
		return self
	
	def __mul__(self, other):
		"""
		Return the Bookmarks object multiplied by an integer.
		
		:param other: The integer value to multiply the Bookmarks object by
		:type other: int
		:return: A Bookmarks object multiplied by an integer
		:rtype: Bookmarks
		"""
		return Bookmarks(self.values * other)
	
	def __imul__(self, other):
		"""
		Concatenate two Bookmarks objects.
		
		:param other: The integer value to multiply the Bookmarks object by
		:type other: int
		:return: A Bookmarks object multiplied by an integer
		:rtype: Bookmarks
		"""
		self.values *= other
		return self
	
	def __str__(self):
		"""
		Return the string representation of the Bookmarks object.
		
		:return: A string representation of the Bookmarks object
		:rtype: str
		"""
		return "<Bookmarks: %r>" % self.values
	
	def __iter__(self):
		"""
		Return an iterator that yields the Bookmarks object's values.
		
		:return: An iterator that returns the