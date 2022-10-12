class LoginDto:
    """
    function creates class LoginDto
    password maxLength: 15 minLength: 4
    returns: None
    """
    def __init__(self, email: str, password: str) -> None:
        self._email = email
        self._password = password

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

