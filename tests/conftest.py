import pytest

from devstack_client import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
