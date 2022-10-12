import pytest
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver. chrome. options import Options
from selenium.webdriver.support.select import Select
import logging
from playwright.sync_api import sync_playwright
import asyncio

from models.GetAuthorDto import GetAuthorDto
from selenium_.s_login_page import Login
from playwright_.p_login_page import Login as p_Login
from apis.account import accountApi
from models.ApiUserDto import ApiUserDto
from models.LoginDto import LoginDto
from models.Author import Author
from models.AutResponseDto import AutResponseDto
from apis.authors import authorsApi
from apis.book import booksApi
from models.Book import  Book
from models.CreateBookDto import CreateBookDto
from models.BookDto import BookDto
from apis.weatherforecast import weatherforecastApi

#----API
@pytest.fixture
def api_url(pytestconfig):
     apiurl = pytestconfig.getoption("--api_url")
     return apiurl
@pytest.fixture
def header(pytestconfig):
    header = pytestconfig.getoption("--header")
    return header




#---API MODELS
@pytest.fixture
def accountapi(api_url,header) -> accountApi:
 #url = "http://localhost:7017/api/"
 api = accountApi(api_url,header)
 return api
@pytest.fixture
def authorapi(api_url,header) -> accountApi:
 #url = "http://localhost:7017/api/"
 api = authorsApi(api_url, header)
 return api
@pytest.fixture
def bookapi(api_url,header) -> booksApi:
 #url = "http://localhost:7017/api/"
 api = booksApi(api_url,header)
 return api
@pytest.fixture
def weatherapi(api_url,header) -> weatherforecastApi:
 #url = "http://localhost:7017/api/"
 api = weatherforecastApi(api_url,header)
 return api





#---DATA
@pytest.fixture
def resgister_account() -> ApiUserDto:
 user= ApiUserDto('vv@sela.co.il', 'string', 'Vered', 'Aharonov')
 return user
@pytest.fixture
def login_vv() -> LoginDto:
 login= LoginDto('vv@sela.co.il', 'string')
 return login
@pytest.fixture
def login_admin() -> LoginDto:
   login= LoginDto('admin@sela.co.il', '123456')
   return login
@pytest.fixture
def post_author() -> dict:
 auth= {"name": "vvvvv","homeLatitude": 1.2,"homeLongitude": 1.5}
 return auth
@pytest.fixture
def put_book_zero_stock() -> BookDto:
 book= BookDto('Animal Farm', 'Animal Farm is a beast fable, in form of satirical allegorical novellaby George Orwell', 50,0,'https://images-na.ssl-images-amazon.com/images/I/91LUbAcpACL.jpg',1,1)
 return book
@pytest.fixture
def post_book() -> CreateBookDto:
 book= CreateBookDto('S.h', 'string', 80,5,'hhh',1)
 return book
@pytest.fixture
def put_author():
 auth= GetAuthorDto('G.O', 26.643, 84.91426,1)
 return auth





#---AUTHENTICATION
@pytest.fixture
def bearer_auth_session(accountapi,login_admin):
    """ bearer authontication
    :param: url -> str
    """
    login = login_admin
    t_header = accountapi.post_login(login=login)
    autho = {'Authorization': f'Bearer {t_header.token}'}
    return autho


#---WEBSITE
@pytest.fixture()
def url(pytestconfig):
    url = pytestconfig.getoption("--url")
    return url
@pytest.fixture()
def frame(pytestconfig):
    frame = pytestconfig.getoption("--framework")
    return frame
@pytest.fixture()
def browser(pytestconfig):
    browser = pytestconfig.getoption("--browser_type")
    return browser
@pytest.fixture()
def driver_path(pytestconfig):
    driver_path = pytestconfig.getoption("--driver_path")
    return driver_path


#---OPEN
@pytest.fixture()
def open(browser,frame,url,driver_path):
 if frame == 'selenium_':
    if browser == 'chrome':
       chrome_options = Options()
       driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
    if browser == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    yield Login(driver)
    driver.close()
 if frame == 'playwright_':
    with sync_playwright() as p:
        if browser == 'firefox':
            browser = p.firefox.launch(headless=False)
        if browser == 'chrome':
            browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        yield p_Login(page)
        page.close()
