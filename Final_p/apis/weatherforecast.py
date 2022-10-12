import json
import requests



class weatherforecastApi():

    def __init__(self, url :str, headers: dict)-> None:
        """function creates class weatherforecastApi
         :returns: None
         """
        self.url = f"{url}"
        self.headers = headers
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def get_weatherforecast(self)->list:
        """
        get weatherforecast
        :returns: List
        """
        res = self.session.get(url=f"{self.url[:-4]}WeatherForecast")
        if res.status_code == 200:
            return res.json()
        else:
            return None

