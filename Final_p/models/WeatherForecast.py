class WeatherForecast:
    """
    function creates class WeatherForecast
    """
    def __init__(self,date: str, temperatureC: int, temperatureF: int, summary: str) -> None:
        self._date = date
        self._temperatureC = temperatureC
        self._temperatureF = temperatureF
        self._summary = summary
