def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, which have a default value
that can be set.

Args:
    user (str): the name of the user for the static authentication
    etcd_host (str): the host for the database.
    etcd_port (int): the port for the database.

Returns:
    dict: the created configuration.
	"""
	config = {}
	config['etcd_host'] = etcd_host
	config['etcd_port'] = etcd_port
	config['user'] = user
	return config

