import os

import keystoneauth1
from openstack import connection


def connect():
    return connection.Connection(
        auth=dict(
            auth_url=os.getenv('AUTH_URL', ''),
            username=os.getenv('USERNAME', ''),
            password=os.getenv('PASSWORD', ''),
            project_id=os.getenv('PROJECT_ID', ''),
            user_domain_name=os.getenv('USER_DOMAIN_NAME', ''),
        ),
        compute_api_version=os.getenv('COMPUTE_API_VERSION', '2'),
        identity_interface=os.getenv('IDENTITY_INTERFACE', 'internal'),
    )


def check_if_authorized(ns):
    def decorator(func):
        def wrapped(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except keystoneauth1.exceptions.http.Unauthorized:
                raise ns.abort(403, 'Invalid keystone credentials provided')

            return result

        return wrapped

    return decorator
