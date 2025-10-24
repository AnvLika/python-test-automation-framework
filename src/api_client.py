import requests


class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"  # Free public API for testing

    def get(self, endpoint, params=None):
        """
        Send a GET request.
        :param endpoint: API endpoint, e.g., "users"
        :param params: Dictionary of query parameters
        :return: Response object
        """
        response = requests.get(f"{self.BASE_URL}/{endpoint}", params=params)
        return response

    def post(self, endpoint, data=None):
        """
        Send a POST request.
        :param endpoint: API endpoint, e.g., "users"
        :param data: Dictionary of payload data
        :return: Response object
        """
        response = requests.post(f"{self.BASE_URL}/{endpoint}", json=data)
        return response
