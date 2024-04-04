def base_config(user, etcd_host="localhost", etcd_port=2379):
    """Creates a configuration with some simple parameters, which have a default value
    that can be set.

    Args:
        user (str): the name of the user for the static authentication
        etcd_host (str): the host for the database.
        etcd_port (int): the port for the database.

    Returns:
        dict: the created configuration.

    """
    return {
        "tls": {
            "enabled": False,
            "cert": "cert_path",
            "key": "key_path",
            "client_ca": "client_ca_path",
        },
        "authentication": {
            "allow_anonymous": True,
            "strategy": {
                "keystone": {"enabled": False, "endpoint": "http://localhost"},
                "keycloak": {
                    "enabled": False,
                    "endpoint": "no_endpoint",
                    "realm": "krake",
                },
                "static": {"enabled": True, "name": user},
            },
            "cors_origin": "http://example.com",
        },
        "authorization": "always-allow",
        "etcd": {"host": etcd_host, "port": etcd_port, "retry_transactions": 0},
        "docs": {"problem_base_url": "http://example.com/problem"},
        "log": {},
    }
