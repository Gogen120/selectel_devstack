from flask_restx import Namespace, Resource

from devstack_client.utils import connect, check_if_authorized, check_required_params
from devstack_client.service.network import list_networks, find_network

ns = Namespace('api/v1/network')


@ns.route('')
class NetworkList(Resource):
    @check_required_params(ns)
    @check_if_authorized(ns)
    def get(self):
        conn = connect()
        networks = list_networks(conn)

        return {
            'networks': networks
        }, 200


@ns.route('/<name>')
class Flavor(Resource):
    @check_required_params(ns)
    @check_if_authorized(ns)
    def get(self, name):
        conn = connect()
        network = find_network(conn, name)

        if network is None:
            ns.abort(404)

        return {
            'network': network
        }, 200
