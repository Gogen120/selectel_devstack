def list_flavors(conn):
    return conn.list_flavors()


def find_flavor(conn, flavor_name):
    return conn.compute.find_flavor(flavor_name)
