import requests
class Base():
    def __init__(self,headers):
        self._headers = headers
        self._session = requests.session()

    def update_session_header(self, headers):
        self._session.headers.update(headers)