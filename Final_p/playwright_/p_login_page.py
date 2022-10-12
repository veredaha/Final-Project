import time
import pytest
from playwright.sync_api import sync_playwright

from playwright_.p_store_page import Store


class Login():

 def __init__(self, driver) -> None:
    """
     function creates Login class
    """

    self._driver = driverr



 locator_dict = {
      "login_btn": 'button >> text=Submit',
      "passwd": '#password',
      "email": '#email',
      "register_btn": 'button >> text=Register!',
      "firstname": '#firstName',
      "lastname": '#lastName',
      "back_to_login": '//*[@id="root"]/div/button',
      "authors_results": '.author-container',
      "books_results": '.book-container',
      "text": '#searchtext',
      "search_btn": 'button >> text=Search',
      "store_btn": '.nav-link >> text=Store',
      "authors_btn": '.nav-link >> text=Authors',
 }

 def login(self,email:str, passwd:str)->Store:
     """
     login to website
     """
     self._driver.locator(self.locator_dict["email"]).fill(email)
     self._driver.locator(self.locator_dict["passwd"]).fill(passwd)
     self._driver.locator(self.locator_dict["login_btn"]).click()
     return Store(self._driver)

 def click_store(self):
     """click on store"""
     self._driver.locator(self.locator_dict["store_btn"]).click()
     return self._driver

 def click_authors(self):
     """click on authors"""
     self._driver.locator(self.locator_dict["authors_btn"]).click()
     return self._driver
 
 
 def register(self,email:str, passwd:str, firstname:str, lastname:str)->Store:
     """
     register to website
     """
     self._driver.locator(self.locator_dict["register_btn"]).click()
     self._driver.locator(self.locator_dict["firstname"]).fill(firstname)
     self._driver.locator(self.locator_dict["lastname"]).fill(lastname)
     self._driver.locator(self.locator_dict["email"]).fill(email)
     self._driver.locator(self.locator_dict["passwd"]).fill(passwd)
     self._driver.locator(self.locator_dict["login_btn"]).click()
     return Store(self._driver)



 def search(self,txt: str):
     """
     search on website, returns results
     """
     self._driver.locator(self.locator_dict["text"]).fill(txt)
     self._driver.locator(self.locator_dict["search_btn"]).click()
     results = []
     authors = self._driver.locator(self.locator_dict["authors_results"])
     books = self._driver.locator(self.locator_dict["books_results"])
     results.extend(authors.all_inner_texts() + books.all_inner_texts())
     return results