class GetAuthorDto:
    """
    function creates class GetAuthorDto
    returns: None
    """
    def __init__(self,name: str, homeLatitude: float, homeLongitude: float, id: int) -> None:
        self._name = name
        self._homeLatitude = homeLatitude
        self._homeLongitude = homeLongitude
        self._id = id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def toJson(self) -> str:
        """
        from class to json
        :returns: str
        """
        result = {}
        for key, val in self.__dict__.items():
            if val is not None:
                if key.startswith("_"):
                    result[key[1:]] = val
                else:
                    result[key] = val
        return result