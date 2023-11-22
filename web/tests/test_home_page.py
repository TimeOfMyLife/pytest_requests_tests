import json
import pytest
from web.pages.locators.home_page_locators import HomePageLocators


@pytest.mark.positive
def test_web_get_list_users(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.USER_LIST)
    status_code = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))
    response_api = api_client_v1.get_list_users(page_number=2).json()

    assert status_code == '200', f"Invalid status code {status_code}, expected 200"
    assert response_web == response_api, f"{response_web} is not {response_api}"


@pytest.mark.positive
def test_web_get_single_user(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.SINGLE_USER)
    status_code = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))
    response_api = api_client_v1.get_single_user(user_id=2).json()

    assert status_code == '200', f"Invalid status code {status_code}, expected 200"
    assert response_web == response_api, f"{response_web} is not {response_api}"


@pytest.mark.negative
def test_web_get_single_user_not_found(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.SINGLE_USER_NOT_FOUND)
    status_code = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))
    response_api = api_client_v1.get_single_user(user_id=23).json()

    assert status_code == '404', f"Invalid status code {status_code}, expected 404"
    assert response_web == response_api, f"{response_web} is not {response_api}"


@pytest.mark.positive
def test_web_get_list_resource(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.LIST_RESOURCE)
    status_code = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))
    response_api = api_client_v1.get_list_resource().json()

    assert status_code == '200', f"Invalid status code {status_code}, expected 200"
    assert response_web == response_api, f"{response_web} is not {response_api}"


@pytest.mark.positive
def test_web_get_single_resource(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.SINGLE_RESOURCE)
    status_code = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))
    response_api = api_client_v1.get_single_resource(user_id=2).json()

    assert status_code == '200', f"Invalid status code {status_code}, expected 200"
    assert response_web == response_api, f"{response_web} is not {response_api}"


@pytest.mark.negative
def test_web_get_single_resource_not_found(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.SINGLE_USER_NOT_FOUND)
    status_code = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))
    response_api = api_client_v1.get_single_resource(user_id='3fd5').json()

    assert status_code == '404', f"Invalid status code {status_code}, expected 404"
    assert response_web == response_api, f"{response_web} is not {response_api}"


@pytest.mark.positive
def test_web_post_create(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.CREATE)

    status_code_web = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))

    data = {"name": "morpheus", "job": "leader"}
    response_api = api_client_v1.post_create(data=data)
    response_api_json = response_api.json()

    assert response_web.keys() == response_api_json.keys(), f"web keys {status_code_web} " \
                                                            f"is not api keys {response_api.status_code}"
    assert status_code_web == str(response_api.status_code), f" web status {status_code_web} " \
                                                             f"is not api status {response_api.status_code}"


@pytest.mark.positive
def test_web_put_update(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.PUT_UPDATE)

    status_code_web = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))

    data = {"name": "ewr", "job": "werwer"}
    response_api = api_client_v1.put_update(data=data, user_id=2)
    response_api_json = response_api.json()

    assert response_web.keys() == response_api_json.keys(), f"web keys {status_code_web} " \
                                                            f"is not api keys {response_api.status_code}"
    assert status_code_web == str(response_api.status_code), f" web status {status_code_web} " \
                                                             f"is not api status {response_api.status_code}"


@pytest.mark.positive
def test_web_patch_update(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.PATCH_UPDATE)

    status_code_web = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))

    data = {"name": "ewr", "job": "werwer"}
    response_api = api_client_v1.patch_update(data=data, user_id=2)
    response_api_json = response_api.json()

    assert response_web.keys() == response_api_json.keys(), f"web keys {status_code_web} " \
                                                            f"is not api keys {response_api.status_code}"
    assert status_code_web == str(response_api.status_code), f" web status {status_code_web} " \
                                                             f"is not api status {response_api.status_code}"


@pytest.mark.positive
def test_web_delete(home_page, api_client_v1):
    home_page.call_request(HomePageLocators.DELETE)

    status_code_web = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))

    response_api = api_client_v1.delete(user_id=2)
    response_api_json = response_api.json()

    assert response_web.keys() == response_api_json.keys(), f"web keys {status_code_web} " \
                                                            f"is not api keys {response_api.status_code}"
    assert status_code_web == str(response_api.status_code), f" web status {status_code_web} " \
                                                             f"is not api status {response_api.status_code}"


@pytest.mark.parametrize("body, expected_status", [
    ({"email": "eve.holt@reqres.in", "password": "pistol"}, '200'),  # Successful registration
    ({"email": "invalid_email", "password": "password"}, '400'),  # Unsuccessful registration
])
def test_web_register(home_page, api_client_v1, body, expected_status):
    if expected_status == '200':
        home_page.call_request(HomePageLocators.REGISTER_SUCCESSFUL)
    else:
        home_page.call_request(HomePageLocators.REGISTER_UNSUCCESSFUL)

    status_code_web = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))

    response_api = api_client_v1.register(data=body)
    response_api_json = response_api.json()

    assert response_web.keys() == response_api_json.keys(), f"web keys {status_code_web} " \
                                                            f"is not api keys {response_api.status_code}"
    assert status_code_web == expected_status, f"web status {status_code_web} is not {expected_status}"
    assert status_code_web == str(response_api.status_code), f"web status {status_code_web} " \
                                                             f"is not api status {response_api.status_code}"


@pytest.mark.parametrize("body, expected_status", [
    ({"email": "eve.holt@reqres.in", "password": "pistol"}, '200'),  # Successful login
    ({"email": "invalid_user@reqres.in", "password": "invalid_password"}, '400'),  # Unsuccessful login
])
def test_web_login(home_page, api_client_v1, body, expected_status):
    if expected_status == '200':
        home_page.call_request(HomePageLocators.LOGIN_SUCCESSFUL)
    else:
        home_page.call_request(HomePageLocators.LOGIN_UNSUCCESSFUL)

    status_code_web = home_page.get_status_code()
    response_web = json.loads(home_page.get_response_body().replace("'", "\""))

    response_api = api_client_v1.login(data=body)
    response_api_json = response_api.json()

    assert response_web.keys() == response_api_json.keys(), f"web keys {status_code_web} " \
                                                            f"is not api keys {response_api.status_code}"
    assert status_code_web == expected_status, f"web status {status_code_web} is not {expected_status}"
    assert status_code_web == str(response_api.status_code), f"web status {status_code_web} " \
                                                             f"is not api status {response_api.status_code}"
