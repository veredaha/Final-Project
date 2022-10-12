import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium_.s_authors_page import Authors
from selenium_.s_store_page import Store


class Login():
 def __init__(self, driver) -> None:
    """
    function creates Login class
    """
    self._driver = driver

 locator_dict = {"email": (By.ID, 'email'),
                 "passwd": (By.ID, 'password'),
                 "login_btn": (By.CSS_SELECTOR, ".container-sm > form > button"),
                 "register_btn": (By.XPATH, "//*[text()='Register!']"),
                 "firstname": (By.ID, 'firstName'),
                 "lastname": (By.ID, 'lastName'),
                 "back_to_login":(By.XPATH, '//*[@id="root"]/div/button'),
                 "authors_btn": (By.XPATH, "//a[@href='/authors']"),
                 "text": (By.ID, "searchtext"),
                 "search_btn": (By.XPATH, "//*/nav/div/form/button"),
                 "authors_results": (By.CLASS_NAME, "author-container"),
                 "books_results": (By.CLASS_NAME, "book-container"),
                 "store_btn": (By.XPATH, "//a[@href='/store']")
                 }



 def login(self,email:str, passwd:str)->Store:
     """
     login to website
     """
     self._driver.find_element(*self.locator_dict["email"]).send_keys(email)
     self._driver.find_element(*self.locator_dict["passwd"]).send_keys(passwd)
     self._driver.find_element(*self.locator_dict["login_btn"]).click()
     return Store(self._driver)

 def register(self,email:str, passwd:str, firstname:str, lastname:str)->Store:
     """
     register to website
     """
     self._driver.find_element(*self.locator_dict["register_btn"]).click()
     self._driver.find_element(*self.locator_dict["firstname"]).send_keys(firstname)
     self._driver.find_element(*self.locator_dict["lastname"]).send_keys(lastname)
     self._driver.find_element(*self.locator_dict["email"]).send_keys(email)
     self._driver.find_element(*self.locator_dict["passwd"]).send_keys(passwd)
     self._driver.find_element(*self.locator_dict["login_btn"]).click()
     return Store(self._driver)



 def click_authors(self):
     """click on authors"""
     self._driver.find_element(*self.locator_dict["authors_btn"]).click()
     return Authors(self._driver)

 def click_store(self):
     """click on store"""
     self._driver.find_element(*self.locator_dict["store_btn"]).click()
     return Store(self._driver)


 def search(self,txt: str):
     """
     search on website, returns results
     """
     self._driver.find_element(*self.locator_dict["text"]).send_keys(txt)
     self._driver.find_element(*self.locator_dict["search_btn"]).click()
     results = []
     authors = self._driver.find_elements(*self.locator_dict["authors_results"])
     books = self._driver.find_elements(*self.locator_dict["books_results"])
     results.extend(authors + books)
     return results