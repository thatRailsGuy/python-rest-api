import falcon
from falcon import testing
import pytest
from unittest.mock import mock_open, call

from rest_api_sample.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_users(client):
    doc = {
        'users': [
            {
                'username': 'user1',
                'email': 'user1@gmail.com'
            }
        ]
    }

    response = client.simulate_get('/users')

    assert response.json == doc
    assert response.status == falcon.HTTP_OK

# "monkeypatch" is a special built-in pytest fixture that can be
# used to install mocks.
def test_posted_image_gets_saved(client, monkeypatch):
    mock_file_open = mock_open()
    monkeypatch.setattr('io.open', mock_file_open)

    fake_uuid = '123e4567-e89b-12d3-a456-426655440000'
    monkeypatch.setattr('uuid.uuid4', lambda: fake_uuid)

    # When the service receives an image through POST...
    fake_image_bytes = b'fake-image-bytes'
    response = client.simulate_post(
        '/users',
        body=fake_image_bytes,
        headers={'content-type': 'application/json'}
    )

    # ...it must return a 201 code, save the file, and return the
    # image's resource location.
    assert response.status == falcon.HTTP_CREATED
    assert call().write(fake_image_bytes) in mock_file_open.mock_calls
    assert response.headers['location'] == '/users/{}.json'.format(fake_uuid)