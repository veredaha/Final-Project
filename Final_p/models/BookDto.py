class BookDto:
    """
    function creates class BookDto
    returns: None
    """
    def __init__(self, name: str, description: str, price: int, amountInStock: int, imageUrl: str , authorId: int,  id: int) -> None:
        self._name = name
        self._description = description
        self._price = price
        self._amountInStock = amountInStock
        self._imageUrl = imageUrl
        self._authorId = authorId
        self._id = id

    @property
    def id(self):
        return self._id

    @property
    def authorId(self):
        return self._authorId

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
