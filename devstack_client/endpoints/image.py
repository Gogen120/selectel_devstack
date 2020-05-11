from flask_restx import Namespace, Resource

from devstack_client.utils import connect, check_if_authorized, check_required_params
from devstack_client.service.image import list_images, find_image

ns = Namespace('api/v1/image')


@ns.route('')
class ImageList(Resource):
    @check_required_params(ns)
    @check_if_authorized(ns)
    def get(self):
        conn = connect()
        images = list_images(conn)

        return {
            'images': images
        }, 200


@ns.route('/<name>')
class Image(Resource):
    @check_required_params(ns)
    @check_if_authorized(ns)
    def get(self, name):
        conn = connect()
        image = find_image(conn, name)

        if image is None:
            ns.abort(404)

        return {
            'image': image
        }, 200
