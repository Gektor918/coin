from rest_framework.test import APIClient
from rest_framework import status


client = APIClient()


def test_all_list_crypto_info():
    response = client.get('/all/info/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['info']) > 0

