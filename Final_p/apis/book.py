import json
import requests
from models.Book import Book
from models.BookDto import BookDto
from models.CreateBookDto import CreateBookDto

from apis.base import Base


class booksApi(Base):

    def __init__(self, url :str, headers: dict)-> None:
        """function creates class booksApi
         :returns: None
         """
        self.url = f"{url}Books/"
        super().__init__(headers)
        self._session.headers.update(self._headers)

    def get_books(self)->list:
        """
        get books
        :returns: List
        """
        res = self._session.get(url=f"{self.url[:-1]}")
        books =[]
        if res.status_code == 200:
            for r in res.json():
                books.append(BookDto(**r))
            return books
        else:
            return None

    def post_book(self, book: CreateBookDto) -> Book:
        """ post new book
        :param: book -> CreateBookDto
        :returns: Book
        """
        res = self._session.post(url=f"{self.url[:-1]}", data=book.toJson())
        if res.status_code == 200:
            return Book(**res.json())
        else:
            return None

    def get_book_by_id(self, id: int) -> BookDto:
        """
         get book by id
        :param: id -> int
        :returns: BookDto"""

        res = self._session.get(url=f"{self.url}{id}")
        if res.status_code == 200:
            return BookDto(**res.json())
        else:
            return None

    def put_book(self, id: int, book :BookDto) -> Book:
        """
        put book
        :param: : int
        :param: book :BookDto
        :returns: book
        """
        res = self._session.put(url=f"{self.url}{id}", data=book.toJson())
        if res.status_code == 200:
            return Book(**res.json())
        else:
            return None


    def delete_book_by_id(self, id:int) :
        """
         delete book by id
        :param: id:int
        """

        res = self._session.delete(url=f"{self.url}{id}")
        if res.status_code == 200:
            return res
        else:
            return None


    def get_book_by_author_id(self, id:int) :
            """
             get book by author id
               :param: id:int
               :returns: BookDto
            """
            res = self._session.get(url=f"{self.url}findauthor/{id}")
            books =[]
            if res.status_code == 200:
                for r in res.json():
                    books.append(BookDto(**r))
                return books
            else:
             return None


    def put_book_id(self, id: int) -> Book:
        """
        put book
        :param: : int
        :returns: book
        """

        res = self._session.put(url=f"{self.url}purchase/{id}")
        if res.status_code == 200:
            return res
        else:
            return None
