import pytest


@pytest.mark.positive
@pytest.mark.parametrize("page_number", [1, 2, 3])
def test_api_get_list_users(api_client_v1, page_number):
    response = api_client_v1.get_list_users(page_number)

    assert response.status_code == 200, f"invalid status code: {response.status_code}," \
                                        f"expected 200"
    assert len(response.json()["data"]) > 0, "missing content 'data'"
    assert response.json()["page"] == page_number, "missing field 'page'"
    assert "per_page" in response.json(), "missing field 'per_page'"
    assert "total" in response.json(), "missing field 'total'"


@pytest.mark.negative
@pytest.mark.parametrize("invalid_page_number", [0, -1, 'abc'])
def test_api_get_list_users_invalid_page(api_client_v1, invalid_page_number):
    response = api_client_v1.get_list_users(invalid_page_number)

    assert response.status_code == 400, f"invalid status code: {response.status_code}," \
                                        f"expected 400"
    assert "error" in response.json(), "missing field 'error'"


@pytest.mark.positive
@pytest.mark.parametrize("user_id, expected_status ", [(1, 200), (3, 200)])
def test_api_get_single_user_positive(api_client_v1, user_id, expected_status):
    response = api_client_v1.get_single_user(user_id)

    actual_data = response.json().get("data")
    actual_support = response.json().get("support")

    expected_fields = {"data":
                           ["id", "email", "first_name", "last_name", "avatar"],
                       "support":
                           ["url", "text"]
                       }

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"
    assert len(response.json()["data"]) > 0, "missing value 'data'"
    assert len(response.json()["support"]) > 0, "missing value 'support'"

    for field in actual_data:
        assert field in expected_fields.get("data"), f"'{field}' missing in response"

    for field in actual_support:
        assert field in expected_fields.get("support"), f"'{field}' missing in response"


@pytest.mark.negative
@pytest.mark.parametrize("user_id", ["65t", "invalid_id", "999"])
def test_api_get_single_user_not_found(api_client_v1, user_id):
    response = api_client_v1.get_single_user(user_id)

    assert response.status_code == 404, f"invalid status code: {response.status_code}," \
                                        f"expected 404"


@pytest.mark.positive
def test_api_get_list_resource(api_client_v1):
    response = api_client_v1.get_list_resource()
    expected_keys = ["page", "per_page", "total", "total_pages", "data", "support"]

    assert response.status_code == 200, f"invalid status code: {response.status_code}," \
                                        f"expected 200"
    assert len(response.json()["data"]) > 0, "missing value 'data'"
    for key in expected_keys:
        assert key in response.json().keys(), f"missing field '{expected_keys}'"


@pytest.mark.positive
@pytest.mark.parametrize("user_id", [1, 2])
def test_api_get_single_resource(api_client_v1, user_id):
    response = api_client_v1.get_single_resource(user_id)

    assert response.status_code == 200, f"invalid status code: {response.status_code}," \
                                        f"expected 200"
    assert "data" in response.json(), "missing field 'data'"
    assert "support" in response.json(), "missing field 'support'"


@pytest.mark.negative
@pytest.mark.parametrize("invalid_user_id", ["2dfg", "xyz", "invalid"])
def test_api_get_single_resource_not_found(api_client_v1, invalid_user_id):
    response = api_client_v1.get_single_resource(invalid_user_id)
    assert response.status_code == 404, f"invalid status code: {response.status_code}," \
                                        f"expected 404"


@pytest.mark.positive
def test_api_post_create(api_client_v1):
    data = {"name": "John Doe", "job": "Software Engineer"}
    response = api_client_v1.post_create(data)

    assert response.status_code == 201, f"invalid status code: {response.status_code}," \
                                        f"expected 201"
    assert "name" in response.json(), "missing field 'name'"
    assert "job" in response.json(), "missing field 'job'"
    assert "id" in response.json(), "missing field 'id'"
    assert "createdAt" in response.json(), "missing field 'createdAt'"


@pytest.mark.negative
def test_api_post_create_bad_request(api_client_v1):
    data = {"job": "Software Engineer"}
    response = api_client_v1.post_create(data)
    assert response.status_code == 400, f"invalid status code: {response.status_code}," \
                                        f"expected 400"


@pytest.mark.positive
@pytest.mark.parametrize("update_data, expected_name, expected_job", [
    ({"name": "Jack"}, "Jack", None),
    ({"job": "user"}, None, "user"),
    ({"name": "Chris", "job": "engineer"}, "Chris", "engineer")
])
def test_api_put_update(api_client_v1, update_data,
                        expected_name, expected_job):
    response = api_client_v1.put_update(update_data, user_id=2)

    assert response.status_code == 200, f"invalid status code: {response.status_code}," \
                                        f"expected 200"
    actual_job = response.json()["job"]
    actual_name = response.json()["name"]
    if "job" in update_data and "name" not in update_data:
        assert actual_job == expected_job, f"wrong value {actual_job}, " \
                                           f"expected {expected_job}"
        assert actual_name is None, f"wrong value {actual_job}, " \
                                    f"expected None"

    elif "name" in update_data and "job" not in update_data:
        assert actual_name == expected_name, f"wrong value {actual_name}, " \
                                             f"expected {expected_name}"

        assert actual_job is None, f"wrong value {actual_name}, " \
                                   f"expected None"

    else:
        assert actual_name == expected_name, f"wrong value {actual_name}, " \
                                             f"expected {expected_name}"
        assert actual_job == expected_job, f"wrong value {actual_name}, " \
                                           f"expected None"


@pytest.mark.positive
@pytest.mark.parametrize("update_data, expected_name, expected_job", [
    ({"name": "Jack"}, "Jack", None),
    ({"job": "user"}, None, "user"),
    ({"name": "Chris", "job": "engineer"}, "Chris", "engineer")
])
def test_api_patch_update(api_client_v1, update_data,
                          expected_name, expected_job):
    initial_response = api_client_v1.get_single_user(user_id=2)
    initial_job = initial_response.json()["data"].get("job")
    initial_name = initial_response.json()["data"].get("name")

    response = api_client_v1.patch_update(update_data, user_id=2)

    assert response.status_code == 200, f"invalid status code: {response.status_code}," \
                                        f"expected 200"
    actual_job = response.json()["job"]
    actual_name = response.json()["name"]

    if "job" in update_data and "name" not in update_data:
        assert actual_job == expected_job, f"wrong value {actual_job}, " \
                                           f"expected {expected_job}"
        assert actual_name == initial_name, f"wrong value {actual_name}, " \
                                            f"expected {initial_name}"

    elif "name" in update_data and "job" not in update_data:
        assert actual_name == expected_name, f"wrong value {actual_name}, " \
                                             f"expected {expected_name}"
        assert actual_job == initial_job, f"wrong value {actual_job}, " \
                                          f"expected {initial_job}"

    else:
        assert actual_name == expected_name, f"wrong value {actual_name}, " \
                                             f"expected {expected_name}"
        assert actual_job == expected_job, f"wrong value {actual_job}, " \
                                           f"expected {expected_job}"


@pytest.mark.positive
@pytest.mark.parametrize("user_id, expected_status", [
    (2, 204),
    (4, 204)
])
def test_api_delete_positive(api_client_v1, user_id, expected_status):
    response = api_client_v1.delete(user_id)

    expected_message = "expected message after successful deletion"

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"
    assert response.text == expected_message, f"invalid message: {response.text}," \
                                              f"expected {expected_message}"


@pytest.mark.negative
@pytest.mark.parametrize("user_id, expected_status", [
    (1324234234, 404),
    (-1, 404)
])
def test_api_delete_negative(api_client_v1, user_id, expected_status):
    response = api_client_v1.delete(user_id)

    expected_message = "expected message after unsuccessful deletion"

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"
    assert response.text == expected_message, f"invalid message: {response.text}," \
                                              f"expected {expected_message}"


@pytest.mark.positive
@pytest.mark.parametrize("test_input, expected_status, expected_fields", [
    ({"email": "eve.holt@reqres.in", "password": "pistol"}, 200, ["id", "token"]),
])
def test_api_post_register_positive(api_client_v1, test_input,
                                    expected_status, expected_fields):
    response = api_client_v1.register(test_input)

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"

    for field in expected_fields:
        assert field in response.json(), f"missing field '{field}'"


@pytest.mark.negative
@pytest.mark.parametrize("test_input, expected_status, expected_error", [
    ({"email": "eve.holt@reqres.in"}, 400, "Missing password"),
    ({"password": "pistol"}, 400, "Missing email or username")
])
def test_api_post_register_negative(api_client_v1, test_input,
                                    expected_status, expected_error):
    response = api_client_v1.register(test_input)
    actual_message = response.json()["error"]

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"
    assert "error" in response.json(), "missing field 'error'"
    assert expected_error in actual_message, f"wrong error message {actual_message}" \
                                             f": expected {expected_error}"


@pytest.mark.positive
@pytest.mark.parametrize("test_input, expected_status, expected_message", [
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, "Login successful"),
])
def test_api_post_login_positive(api_client_v1, test_input,
                                 expected_status, expected_message):
    response = api_client_v1.login(test_input)

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"
    assert "token" in response.json(), "missing field 'token'"


@pytest.mark.negative
@pytest.mark.parametrize("test_input, expected_status, expected_message", [
    ({"email": "eve.holt@reqres.in"}, 400, "Missing password"),
    ({"password": "pistol"}, 400, "Missing email or username")
])
def test_api_post_login_negative(api_client_v1, test_input,
                                 expected_status, expected_message):
    response = api_client_v1.login(test_input)

    assert response.status_code == expected_status, f"invalid status code: {response.status_code}," \
                                                    f"expected {expected_status}"
    assert "error" in response.json(), "missing field 'error'"
    assert expected_message in response.json()["error"], f"wrong error message {response.json()['error']}" \
                                                         f": expected {expected_message}"
