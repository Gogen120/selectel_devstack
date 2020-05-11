from flask import Flask

from devstack_client.endpoints import server, image, flavor, network
from devstack_client.extensions import api


def init_extensions(app):
    api.init_app(app, title="Devstack Client API", version="0.0.1")


def init_api(api):
    api.add_namespace(server.ns)
    api.add_namespace(image.ns)
    api.add_namespace(flavor.ns)
    api.add_namespace(network.ns)


def create_app():
    app = Flask(__name__)

    app.config.from_object('devstack_client.config')

    init_extensions(app)
    init_api(api)

    return app
