import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver. chrome. options import Options
from selenium.webdriver.support.select import Select
import logging
from fixtures_sp import *
from playwright.sync_api import sync_playwright
import asyncio
from selenium_.s_login_page import Login
from playwright_.p_login_page import Login as p_Login
from selenium_.s_store_page import Store
from selenium_.s_authors_page import Authors
import time
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

def test_books_on_store(open,bookapi)->None:
    mylogger.info("test for books in store on website and api")
    login_page = open.login('admin@sela.co.il','123456')
    time.sleep(3)
    books_s = login_page.store_books()
    books = bookapi.get_books()
    assert len(books) == len(books_s)

def test_purchasing_book(open,bookapi)->None:
    mylogger.info("test for purchasing a book on website ")
    store_page = open.login('admin@sela.co.il','123456')
    time.sleep(3)
    buy = store_page.purchase_book(2)
    msg,stock = buy.msg_after_purchase()
    assert 'Thank you for your purchase' in msg
    assert 'Left In Stock: 9Purchase' in stock

def test_purchasing_book_without_login(open,bookapi)->None:
    mylogger.info("test for purchasing a book without loging in on website ")
    store = open.click_store()
    time.sleep(3)
    buy = store.purchase_book(2)
    msg,stock = buy.msg_after_purchase()
    assert 'Must be signed in to purchase.' in msg

def test_delete_book(open,bookapi,bearer_auth_session)->None:
    mylogger.info("test for deleting a book on website and api ")
    bookapi.update_session_header(bearer_auth_session)
    bookapi.delete_book_by_id(2)
    store = open.click_store()
    books_s = store.store_books()
    books = bookapi.get_books()
    assert len(books) == len(books_s)

def test_put_book_stock_zero(open,bookapi,bearer_auth_session,put_book_zero_stock):
    mylogger.info("test for deleting a book on website and api ")
    bookapi.update_session_header(bearer_auth_session)
    account = bookapi.put_book(1, put_book_zero_stock)
    store_page = open.login('admin@sela.co.il', '123456')
    time.sleep(3)
    buy = store_page.purchase_book(1)
    msg, stock = buy.msg_after_purchase()
    #fix
    assert 'Thank you for your purchase' in msg