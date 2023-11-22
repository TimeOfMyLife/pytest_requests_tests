import requests


class ApiClientV1:

    def __init__(self):
        self.base_url_v1 = 'https://reqres.in/api'

    def get_list_users(self, page_number):
        url = f"{self.base_url_v1}/users?page={page_number}"
        response = requests.get(url)
        return response

    def get_single_user(self, user_id):
        url = f"{self.base_url_v1}/users/{user_id}"
        response = requests.get(url)
        return response

    def get_list_resource(self):
        url = f"{self.base_url_v1}/unknown"
        response = requests.get(url)
        return response

    def get_single_resource(self, user_id):
        url = f"{self.base_url_v1}/unknown/{user_id}"
        response = requests.get(url)
        return response

    def post_create(self, data):
        url = f"{self.base_url_v1}/users"
        response = requests.post(url, data=data)
        return response

    def put_update(self, data, user_id=None):
        url = f"{self.base_url_v1}/users/{user_id}"
        response = requests.put(url, data)
        return response

    def patch_update(self, data, user_id=None):
        url = f"{self.base_url_v1}/users/{user_id}"
        response = requests.patch(url, data=data)
        return response

    def delete(self, user_id):
        url = f"{self.base_url_v1}/users/{user_id}"
        response = requests.delete(url)
        return response

    def register(self, data):
        url = f"{self.base_url_v1}/register"
        response = requests.post(url, data=data)
        return response

    def login(self, data):
        url = f"{self.base_url_v1}/login"
        response = requests.post(url, data=data)
        return response
