import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Authors():
 def __init__(self, _driver) -> None:
    """
    function creates Authors class
    """
    self._driver = _driver



 locator_dict = {"author": (By.CLASS_NAME, "author-container"),
                 "to_author_page": (By.CSS_SELECTOR, "div.card-footer > button"),
                 "author_name": (By.CSS_SELECTOR, ".card-body > .card-title"),
                 "author_name_text": (By.CSS_SELECTOR, "h1 > .badge"),
                 "books_list": (By.CLASS_NAME, 'book-container')}

 def authors_of_the_store(self):
     """
     returns all the authors on authors page
     """
     return self._driver.find_elements(*self.locator_dict["author"])

 def author_name(self, num: int):
     """
     returns all the author name
     """
     return self.authors_of_the_store()[num].find_element(*self.locator_dict["author_name"]).text

 def author_books(self):
     """
     returns all the author's book
     """
     return self._driver.find_elements(*self.locator_dict["books_list"])


 def to_author_page(self, num: int):
     """
     takes you to a specific author page
     """
     self.authors_of_the_store()[num].find_element(*self.locator_dict["to_author_page"]).click()
     return Authors(self._driver)



