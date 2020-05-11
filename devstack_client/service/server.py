def list_servers(conn):
    return conn.list_servers()


def find_server(conn, server_id):
    return conn.get_server_by_id(server_id)


def delete_server(conn, server_id):
    return conn.delete_server(server_id, wait=True)


def get_server_info(server):
    return {
        'id': server.get('id'),
        'name': server.get('name'),
        'addresses': server.get('addresses'),
    }
