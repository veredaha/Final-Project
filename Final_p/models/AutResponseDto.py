class AutResponseDto:
    """
    function creates class AutResponseDto
    returns: None
    """
    def __init__(self, userId: str, token: str, refreshToken: str) -> None:
        self._userId = userId
        self._token = token
        self._refreshToken = refreshToken

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

    @property
    def userId(self):
        return self._userId

    @property
    def token(self):
        return self._token