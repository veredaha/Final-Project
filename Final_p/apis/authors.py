import json
import requests
from models.Author import Author
from models.GetAuthorDto import GetAuthorDto

from apis.base import Base


class authorsApi(Base):

    def __init__(self, url: str, headers: dict) -> None:
        """function creates class authorsApi
         :returns: None
         """
        self.url = f"{url}Authors/"
        super().__init__(headers)
        self._session.headers.update(self._headers)


    def get_authors(self)->list:
        """
        get authors
        :returns: list
        """
        res = self._session.get(url=f"{self.url[:-1]}")
        authors = []
        if res.status_code == 200:
            for r in res.json():
                authors.append(GetAuthorDto(**r))
            return authors
        else:
            return None

    def post_author(self, auth :Author) ->Author:
        """
        post author
        :returns: Author
        """
        res = self._session.post(url=f"{self.url[:-1]}", json=auth)
        if res.status_code == 200:
            return Author(**res.json())
        else:
            return None


    def get_authors_by_id(self,id:int)->Author:
        """ get authors by id
        :returns: Author
        """
        res = self._session.get(url=f"{self.url}{id}")
        if res.status_code == 200:
            return Author(**res.json())
        else:
            return None

    def put_author(self, id: int, auth :GetAuthorDto)-> Author:
     """
     put_author
     :returns: Author
     """
     res = self._session.put(url=f"{self.url}{id}", data=auth.toJson())
     if res.status_code == 200:
        return Author(**res.json())
     else:
        return None

    def delete_author(self, id: int) :
         """
         delete author
         """
         res = self._session.delete(url=f"{self.url}{id}")
         if res.status_code == 200:
             return res
         else:
             return None

    def get_author_by_search(self, text: str) -> Author:
        """ get author by search
           :param: text: str
           """
        res = self._session.get(url=f"{self.url}search/{text}")
        if res.status_code == 200:
            return Author(**res.json())
        else:
            return None


