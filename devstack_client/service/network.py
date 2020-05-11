def list_networks(conn):
    return conn.list_networks()


def find_network(conn, network_name):
    return conn.network.find_network(network_name)
