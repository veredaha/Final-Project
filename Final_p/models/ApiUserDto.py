class ApiUserDto():
    """
    function creates class ApiUserDto
    password maxLength: 15 minLength: 4
    returns: None
    """
    def __init__(self, email: str, password: str, firstName: str, lastName: str) -> None:
        self._email = email
        self._password = password
        self._firstName = firstName
        self._lastName = lastName

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
