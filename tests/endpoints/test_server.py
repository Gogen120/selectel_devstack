from unittest.mock import patch


@patch('devstack_client.endpoints.server.list_servers')
def test_get_all_servers(mock_list_servers, client):
    mock_list_servers.return_value = [
        {
            'addresses': {
                'public': [
                    {
                        "addr": "172.24.4.74",
                        "version": 4
                    },
                    {
                        "addr": "2001:db8::1da",
                        "version": 6
                    }
                ]
            },
            'id': '1',
            'name': 'mock_server',
        },
    ]
    res = client.get('/api/v1/server')

    assert res.status_code == 200
    assert len(res.json.get('servers')) == 1


@patch('devstack_client.endpoints.server.find_server')
def test_get_server(mock_find_server, client):
    mock_find_server.return_value = {
        'addresses': {
            'public': [
                {
                    "addr": "172.24.4.74",
                    "version": 4,
                },
                {
                    "addr": "2001:db8::1da",
                    "version": 6,
                }
            ]
        },
        'id': '1',
        'name': 'mock_server',
    }

    res = client.get('/api/v1/server/mock_server')

    assert res.status_code == 200
    assert res.json.get('server').get('name') == 'mock_server'
    assert res.json.get('server').get('id') == '1'


@patch('devstack_client.endpoints.server.find_server')
def test_get_non_existing_server(mock_find_server, client):
    mock_find_server.return_value = None

    res = client.get('/api/v1/server/mock_server')

    assert res.status_code == 404
