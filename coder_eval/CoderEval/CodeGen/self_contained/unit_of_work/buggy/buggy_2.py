def unit_of_work(metadata=None, timeout=None):
	"""
	This function is a decorator for transaction functions that allows extra control over how the transaction is carried out.

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
:type timeout: float or :const:`None`
	"""
	def decorator(func):
		if metadata is None:
			metadata = {}
		else:
			metadata = dict(metadata)
		if timeout is not None:
			timeout = int(timeout)
		if timeout is None:
			timeout = default_timeout
		if timeout < 0:
			raise ValueError("timeout must be a positive non-zero number")
		def wrapper(*args, **kwargs):
			tx = Transaction(func, metadata=metadata, timeout=timeout, *args, **kwargs)
			tx.run()
			return tx
		return wrapper
	return decorator

