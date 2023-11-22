import pytest
from api.client_api_v1 import ApiClientV1


@pytest.fixture(scope="session")
def api_client_v1():
    return ApiClientV1()
