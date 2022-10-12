import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_.s_authors_page import Authors



class Store():
 def __init__(self, driver) -> None:
    """
    function creates Store class
    """
    self._driver = driver

 locator_dict = {"book": (By.CLASS_NAME, "book-container"),
                 "purchase_button": (By.CSS_SELECTOR, "div.card-footer > button"),
                 "book_name": (By.CSS_SELECTOR, ".card-body > .card-title"),
                 "author_name_title": (By.CSS_SELECTOR, "h1 > .badge"),
                 'check_page' : (By.XPATH,"//*[@id='root']/div"),
                 'check_page_invalid':(By.XPATH, "//*[@id='root']/div/form/div[1]/small"),
                 "authors_btn": (By.XPATH, "//a[@href='/authors']"),
                 "books_list": (By.CLASS_NAME, 'book-container'),
                 "purchase" :(By.CSS_SELECTOR, "div.card-footer > button"),
                 "stock":(By.CLASS_NAME,"card-footer")


                 }

 def purchase_book(self, num: int):
     """
     purchase a book
     """
     book = self._driver.find_elements(*self.locator_dict["book"])[num]
     book.find_element(*self.locator_dict["purchase"]).send_keys(Keys.ENTER)
     return Store(self._driver)

 def book_name(self, num) -> int:
    """
    returns book name
    """
    return self.books_of_the_store()[num].find_element(*self.locator_dict["book_name"]).text

 def click_authors(self):
     """click on authors"""
     self._driver.find_element(*self.locator_dict["authors_btn"]).click()
     return Authors(self._driver)

 def msg_after_purchase(self) -> str:
        """
        returns the text inside alert box after purchasing
        """
        alert = self._driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        stock = self._driver.find_element(*self.locator_dict["stock"]).text
        return alert_text, stock

 def book_amount(self, num: int) -> int:
        """
        returns the amount of books that left in the store
        """
        book_details = self.books_of_the_store()[num].text
        book_details_filter = book_details.replace('Purchase', '')
        return int(book_details_filter[-1])


 def store_books(self):
     """
     returns all the books in the store
     """
     return self._driver.find_elements(*self.locator_dict["books_list"])



