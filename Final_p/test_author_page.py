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


def test_find_author_books(open,bookapi)->None:
    mylogger.info("test for finding author books on website and api")
    authors_page = open.click_authors()
    author = authors_page.to_author_page(1)
    books = author.author_books()
    b = bookapi.get_book_by_author_id(1)
    assert len(books) == len(b)


def test_find_post_author_books(open,authorapi,bookapi,bearer_auth_session,post_book)->None:
    mylogger.info("test for posting author books on website and api")
    authorapi.update_session_header(bearer_auth_session)
    book = bookapi.post_book(post_book)
    authors_page = open.click_authors()
    author = authors_page.to_author_page(1)
    books = author.author_books()
    b = bookapi.get_book_by_author_id(1)
    assert len(books) == len(b)