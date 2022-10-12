class ProblemDetails:
    """
    function creates class ProblemDetails
    returns: None
    """
    def __init__(self, type: str, title: str, status: str, detail: str, instance: str) -> None:
        self._type = type
        self._title = title
        self._status = status
        self._detail = detail
        self._instance = instance