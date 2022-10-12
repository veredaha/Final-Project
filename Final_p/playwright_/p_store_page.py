import time
import pytest
from playwright.sync_api import sync_playwright

from playwright_.p_authors_page import Authors


class Store():

 def __init__(self, driver) -> None:
    """
     function creates Store class
    """
    self._driver = driver



 locator_dict = { "list": '.store-container >> .book-container',
                  "purchase_btn": 'div.card-footer >> button',
                  "book_name": '.card-body >> .card-title',
                  'check_page_invalid': "//*[@id='root']/div/form/div[1]/small",
                  "authors_btn": '.nav-link >> text=Authors',
                  'check_page': "//*[@id='root']/div",

                  }

 def purchase_book(self, num: int):
     """
     purchase a book
     """
     list = self._driver.locator(self.locator_dictionary["list"])
     list.nth(num).locator(self.locator_dictionary["purchase_btn"]).click()
     return Store(self._driver)


 def book_name(self, num: int) :
     """
     returns book name
     """
     return self.books_of_the_store().nth(num).locator(self.locator_dict["book_name"]).inner_text()

 def click_authors(self):
     """click on authors"""
     self._driver.locator(self.locator_dict["authors_btn"]).click()
     return Authors(self._driver)

 def book_amount(self, num: int):
     """
     returns the amount of books that left in the store
     """
     book_details = self.store_books().nth(num).inner_text()
     book_details_filter = book_details.replace('Purchase', '')
     return int(book_details_filter[-1])

 def store_books(self):
     """
     returns all the books in the store
     """
     return self._driver.locator(self.locator_dict["book_card"])

