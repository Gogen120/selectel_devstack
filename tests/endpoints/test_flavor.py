from unittest.mock import patch


@patch('devstack_client.endpoints.flavor.list_flavors')
def test_get_all_flavors(mock_list_flavors, client):
    mock_list_flavors.return_value = [
        {
            'flavor_name': 'mock_flavor',
        },
        {
            'flavor_name': 'another_mock_flavor',
        },
    ]
    res = client.get('/api/v1/flavor')

    assert res.status_code == 200
    assert len(res.json.get('flavors')) == 2


@patch('devstack_client.endpoints.flavor.find_flavor')
def test_get_flavor(mock_find_flavor, client):
    mock_find_flavor.return_value = {'flavor_name': 'mock_flavor'}

    res = client.get('/api/v1/flavor/mock_flavor')

    assert res.status_code == 200
    assert res.json.get('flavor').get('flavor_name') == 'mock_flavor'


@patch('devstack_client.endpoints.flavor.find_flavor')
def test_get_non_existing_flavor(mock_find_flavor, client):
    mock_find_flavor.return_value = None

    res = client.get('/api/v1/flavor/mock_flavor')

    assert res.status_code == 404
