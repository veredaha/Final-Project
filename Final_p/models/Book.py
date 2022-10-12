class Book:
    """
    function creates class Book
    returns: None
    """
    def __init__(self, id: int, name: str, description: str, price: int, amountInStock: int, imageUrl: str , authorId: int, author: 'Author') -> None:
        self._id = id
        self._name = name
        self._description = description
        self._price = price
        self._amountInStock = amountInStock
        self._imageUrl = imageUrl
        self._authorId = authorId
        self._author = author

    @property
    def id(self):
        return self._id

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





