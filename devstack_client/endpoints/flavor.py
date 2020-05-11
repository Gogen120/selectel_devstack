from flask_restx import Namespace, Resource

from devstack_client.utils import connect, check_if_authorized
from devstack_client.service.flavor import list_flavors, find_flavor

ns = Namespace('api/v1/flavor')


@ns.route('')
class FlavorList(Resource):
    @check_if_authorized(ns)
    def get(self):
        conn = connect()
        flavors = list_flavors(conn)

        return {
            'flavors': flavors
        }, 200


@ns.route('/<name>')
class Flavor(Resource):
    @check_if_authorized(ns)
    def get(self, name):
        conn = connect()
        flavor = find_flavor(conn, name)

        if flavor is None:
            ns.abort(404)

        return {
            'flavor': flavor
        }, 200
