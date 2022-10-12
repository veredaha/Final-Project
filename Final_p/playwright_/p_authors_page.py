import time
import pytest
from playwright.sync_api import sync_playwright



class Authors():

 def __init__(self, driver) -> None:
    """
     function creates Authors class
    """
    self._driver = driver



 locator_dict = { "author": '.author-container',
                  "to_author_page": 'div.card-footer >> button',
                  "author_name": '//*[@id="root"]/div/h1/span',
                  "book_list": '.book-container',}

 def authors_of_the_store(self):
     """
     returns all the authors on authors page
     """
     return self._driver.locator(self.locator_dict["author"])

 def author_name(self, num: int):
     """
     returns all the author name
     """
     return self.authors_of_the_store().nth(num).locator(self.locator_dict["author_name"]).inner_text()

 def author_books(self):
     """
     returns all the author's book
     """
     return self._drive.locator(self.locator_dict["book_list"])

 def to_author_page(self, num: int):
     """
     takes you to a specific author page
     """
     self.authors_of_the_store().nth(num).locator(self.locator_dict["to_author_page"]).click()
     return Authors(self._driver)

