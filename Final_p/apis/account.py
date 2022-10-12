
import json
import requests
from models.ApiUserDto import ApiUserDto
from models.LoginDto import LoginDto
from models.AutResponseDto import AutResponseDto



class accountApi():

    def __init__(self, url :str, headers: dict)-> None:
        """function creates class accountApi
         :returns: None 
         """
        self.url = f"{url}Account/"
        self.headers = headers
        self.session = requests.session()
        self.session.headers.update(self.headers)


    def post_account(self,account:ApiUserDto):
        """ post account
        :param:account->ApiUserDto
         """
        res = self.session.post(url=f"{self.url}register", json=account.toJson())
        if res.status_code == 200:
            return res
        else:
            return None

    def post_login(self, login :LoginDto)-> AutResponseDto:
        """ post login
        :param:login :LoginDto
         """
        res = self.session.post(url=f"{self.url}login", json=login.toJson())
        if res.status_code == 200:
            return AutResponseDto(**res.json())
        else:
            return None

    def post_refreshtoken(self,user :AutResponseDto) -> AutResponseDto:
        """ refresh token
        :param:auth :AutResponseDto
         """
        res = self.session.post(url=f"{self.url}refreshtoken", json=user.toJson())
        return AutResponseDto(**res.json())



