def unit_of_work(metadata=None, timeout=None):

	"""This function is a decorator for transaction functions that allows extra control over how the transaction is carried out.

For example, a timeout may be applied::

    from neo4j import unit_of_work

    @unit_of_work(timeout=100)
    def count_people_tx(tx):
        result = tx.run("MATCH (a:Person) RETURN count(a) AS persons")
        record = result.single()
        return record["persons"]

:param metadata:
    a dictionary with metadata.
    Specified metadata will be attached to the executing transaction and visible in the output of ``dbms.listQueries`` and ``dbms.listTransactions`` procedures.
    It will also get logged to the ``query.log``.
    This functionality makes it easier to tag transactions and is equivalent to ``dbms.setTXMetaData`` procedure, see https://neo4j.com/docs/operations-manual/current/reference/procedures/ for procedure reference.
:type metadata: dict

:param timeout:
    the transaction timeout in seconds.
    Transactions that execute longer than the configured timeout will be terminated by the database.
    This functionality allows to limit query/transaction execution time.
    Specified timeout overrides the default timeout configured in the database using ``dbms.transaction.timeout`` setting.
    Value should not represent a negative duration.
    A zero duration will make the transaction execute indefinitely.
    None will use the default timeout configured in the database.
:type timeout: float or :const:`None`"""
	if metadata is not None and not isinstance(metadata, dict):
		raise TypeError("metadata must be a dict")
	if timeout is not None and not isinstance(timeout, (int, float)):
		raise TypeError("timeout must be a float or None")

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			# We could use inspect.getcallargs to get the correct set of
			# arguments and pass those to begin_transaction, but that would
			# mean we break if the number or type of arguments to the
			# decorated function changes.
			connection = args[0]
			if not isinstance(connection, Connection):
				raise TypeError("unit_of_work must only be applied to functions that have a Connection instance as their first argument")
			if len(args) > 1 or kwargs:
				# The function has more arguments than just the connection,
				# so we need to bind them to
