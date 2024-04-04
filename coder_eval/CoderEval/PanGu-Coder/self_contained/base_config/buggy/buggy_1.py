def base_config(user, etcd_host="localhost", etcd_port=2379):
    config = {"user": user, "etcd_host": etcd_host, "etcd_port": etcd_port}
    return config
