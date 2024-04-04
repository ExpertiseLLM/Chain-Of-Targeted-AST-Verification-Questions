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
	if not metadata:
		metadata = {}
	if timeout is not None:
		metadata = {**metadata, **{'timeout': timeout}}
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			tx = func(*args, **kwargs)
			tx.unit_of_work(**metadata)
			return tx
		return wrapper
	return decorator

from neo4j.orm import GraphDatabase, GraphType

class Graph:
	def __init__(self, uri, user=None, password=None, graph_type=GraphType.TRANSACTION):
		self._driver = GraphDatabase(uri, user, password, graph_type=graph_type)
		self._transaction = None
		self._metadata = None
	
	def run_transaction(self, tx, **kwargs):
		"""
		Runs a transaction with the given parameters and returns the transaction object.
		
		:param tx: a :class:`neo4j.orm.Transaction` object.
		:param kwargs: additional arguments, see :py:meth:`neo4j.orm.Transaction.run_tx`.
		
		:return: the transaction object.
		"""
		tx.run(tx.tx.tx, **kwargs)
		return self._transaction
	
	def list_transactions(self, tx=None):
		"""
		Lists the transactions in the given transaction. Returns the list of transactions if ``tx`` is None.
		
		:param tx: a :class:`neo4j.orm.Transaction` object.
		
		:return: the list of transactions in the database.
		"""
		tx = self.run_transaction(tx, tx=tx)
		return tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.tx.