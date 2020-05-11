from openstack.exceptions import ResourceFailure

from flask_restx import Namespace, Resource, fields

from devstack_client.utils import connect, check_if_authorized, check_required_params
from devstack_client.service.server import list_servers, find_server, get_server_info, delete_server
from devstack_client.service.image import find_image
from devstack_client.service.flavor import find_flavor
from devstack_client.service.network import find_network


ns = Namespace('api/v1/server')

server_post = ns.model('Server', {
    'name': fields.String(required=True, description='Name of the new server'),
    'image': fields.String(required=True, description='which image to use to create a new server'),
    'flavor': fields.String(required=True, description='which flavor to use to create a new server'),
    'network': fields.String(required=True, description='which network to use to create a new server'),
})


@ns.route('')
class ServerList(Resource):
    @check_required_params(ns)
    @check_if_authorized(ns)
    def get(self):
        conn = connect()
        server_info = []
        for server in list_servers(conn):
            server_info.append(get_server_info(server))

        return {
            'servers': server_info
        }, 200

    @ns.expect(server_post)
    @check_required_params(ns)
    @check_if_authorized(ns)
    def post(self):
        conn = connect()
        image = find_image(conn, ns.payload.get('image'))
        if image is None:
            ns.abort(400, f'Invalid image provided: {ns.payload.get("image")}')

        flavor = find_flavor(conn, ns.payload.get('flavor'))
        if flavor is None:
            ns.abort(400, f'Invalid flavor provided: {ns.payload.get("flavor")}')

        network = find_network(conn, ns.payload.get('network'))
        if network is None:
            ns.abort(400, f'Invalid network provided: {ns.payload.get("network")}')

        try:
            server = conn.compute.create_server(
                name=ns.payload.get('name'), image_id=image.id,
                flavor_id=flavor.id, networks=[{"uuid": network.id}],
            )
            server = conn.compute.wait_for_server(server)
        except ResourceFailure:
            raise ns.abort(400, "Invalid resources provided. Check if you have enough resources left on devstack machine")

        return {
            'server': server,
        }, 201


@ns.route('/<server_id>')
class Server(Resource):
    @check_required_params(ns)
    @check_if_authorized(ns)
    def get(self, server_id):
        conn = connect()
        server = find_server(conn, server_id)

        if server is None:
            ns.abort(404)

        return {
            'server': get_server_info(server)
        }, 200

    @check_required_params(ns)
    @check_if_authorized(ns)
    def delete(self, server_id):
        conn = connect()
        server = find_server(conn, server_id)

        if server is None:
            ns.abort(404)

        success = delete_server(conn, server_id)

        return {
            'server': server,
            'success': success,
        }, 200
