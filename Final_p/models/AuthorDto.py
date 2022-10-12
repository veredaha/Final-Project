class AuthorDto:
    """
    function creates class AuthorDto
    returns: None
    """
    def __init__(self, id: int, name: str, homeLatitude: float, homeLongitude: float, books: list) -> None:
        self._id = id
        self._name = name
        self._homeLatitude = homeLatitude
        self._homeLongitude = homeLongitude
        self._books = books