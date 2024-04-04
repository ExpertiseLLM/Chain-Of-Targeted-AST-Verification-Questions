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
	config = {
		"user": user,
		"etcd_host": etcd_host,
		"etcd_port": etcd_port,
		"etc_type": "database",
		"etc_server": "test",
		"etc_name": "test",
		"etc_password": "test",
		"etc_host": "localhost",
		"etc_port": 2379,
		"etc_timeout": 30,
		"etc_max_age": 120,
		"etc_max_length": 128,
		"etc_type_size": 10,
		"etc_type_max_size": 10,
		"etc_type_min_size": 10,
		"etc_type_default": "string",
		"etc_type_size_default": 10,
		"etc_type_max_size_default": 10,
		"etc_type_min_size_default": 10,
		"etc_type_default_default": "string",
		"etc_type_size_default_default": 10,
		"etc_type_min_size_default_default": 10,
		"etc_type_default_default_default": "string",
		"etc_type_size_default_default_default": 10,
		"etc_type_min_size_default_default_default": 10,
		"etc_type_default_default_default_default": "string",
		"etc_type_size_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default": 10,
		"etc_type_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default_default_default": "string",
		"etc_type_size_default_default_default_default_default_default_default": 10,
		"etc_type_min_size_default_default_default_default_default_default_default": 10,
		"etc_type_default_default_default_default_default_default_default_default": "