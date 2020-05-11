from unittest.mock import patch


@patch('devstack_client.endpoints.image.list_images')
def test_get_all_images(mock_list_images, client):
    mock_list_images.return_value = [
        {
            'image_name': 'mock_image',
        },
        {
            'image_name': 'another_mock_image',
        },
    ]
    res = client.get('/api/v1/image')

    assert res.status_code == 200
    assert len(res.json.get('images')) == 2


@patch('devstack_client.endpoints.image.find_image')
def test_get_image(mock_find_image, client):
    mock_find_image.return_value = {'image_name': 'mock_image'}

    res = client.get('/api/v1/image/mock_image')

    assert res.status_code == 200
    assert res.json.get('image').get('image_name') == 'mock_image'


@patch('devstack_client.endpoints.image.find_image')
def test_get_non_existing_image(mock_find_image, client):
    mock_find_image.return_value = None

    res = client.get('/api/v1/image/mock_image')

    assert res.status_code == 404
