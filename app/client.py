from random import randint

import requests


class AppClient:
    URL = 'http://0.0.0.0:5000/'
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_path(self, path: str) -> str:
        response = self._session.get(self.URL + path, timeout=self.TIMEOUT)
        return response.text

    def path_one(self) -> str:
        path = 'one'
        return self.get_path(path)

    def path_two(self) -> str:
        path = 'two'
        return self.get_path(path)

    def path_three(self) -> str:
        path = 'three'
        return self.get_path(path)

    def path_four(self) -> str:
        path = 'four'
        return self.get_path(path)

    def path_five(self) -> str:
        path = 'five'
        return self.get_path(path)

    def path_error(self) -> str:
        path = 'error'
        return self.get_path(path)


if __name__ == '__main__':
    client = AppClient()
    methods = ["path_one",
               "path_two",
               "path_three",
               "path_four",
               "path_five",
               "path_error"]
    for method in methods:
        func = getattr(client, method)
        for _ in range(1, randint(1, 10)):
            func()
