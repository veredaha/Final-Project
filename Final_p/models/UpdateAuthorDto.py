class UpdateAuthorDto:
    """
    function creates class UpdateAuthorDto
    """
    def __init__(self,name: str, homeLatitude: float, homeLongitude: float, id: int) -> None:
        self._name = name
        self._homeLatitude = homeLatitude
        self._homeLongitude = homeLongitude
        self._id = id