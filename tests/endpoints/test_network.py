from unittest.mock import patch


@patch('devstack_client.endpoints.network.list_networks')
def test_get_all_network(mock_list_networks, client):
    mock_list_networks.return_value = [
        {
            'network_name': 'mock_network',
        },
        {
            'network_name': 'another_mock_network',
        },
    ]
    res = client.get('/api/v1/network')

    assert res.status_code == 200
    assert len(res.json.get('networks')) == 2


@patch('devstack_client.endpoints.network.find_network')
def test_get_network(mock_find_network, client):
    mock_find_network.return_value = {'network_name': 'mock_network'}

    res = client.get('/api/v1/network/mock_network')

    assert res.status_code == 200
    assert res.json.get('network').get('network_name') == 'mock_network'


@patch('devstack_client.endpoints.network.find_network')
def test_get_non_existing_network(mock_find_network, client):
    mock_find_network.return_value = None

    res = client.get('/api/v1/network/mock_network')

    assert res.status_code == 404
