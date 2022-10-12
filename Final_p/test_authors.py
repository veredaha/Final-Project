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


def test_count_authors(open,authorapi)->None:
    mylogger.info("test for getting authors on website and api")
    authors_page = open.click_authors()
    authors = authors_page.authors_of_the_store()
    res = authorapi.get_authors()
    assert len(authors) == len(res)

def test_add_and_count_authors(open,authorapi,bearer_auth_session,post_author)->None:
    mylogger.info("test for adding an author on api and getting authors on website and api")
    authorapi.update_session_header(bearer_auth_session)
    author = authorapi.post_author(post_author)
    authors_page = open.click_authors()
    authors = authors_page.authors_of_the_store()
    res = authorapi.get_authors()
    assert len(authors) == len(res)

def test_update_and_check_authors(open,authorapi,bearer_auth_session,put_author)->None:
    mylogger.info("test for updating an author on api and getting authors on website and api")
    authorapi.update_session_header(bearer_auth_session)
    author =  authorapi.put_author(1,put_author)
    authors_page = open.click_authors()
    authors = authors_page.author_name(1)
    assert authors == 'G.O'


def test_delete_and_check_authors(open,authorapi,bearer_auth_session,put_author,post_author)->None:
    mylogger.info("test for deleting an author on api and getting authors on website and api")
    authorapi.update_session_header(bearer_auth_session)
    author = authorapi.post_author(post_author)
    res = authorapi.delete_author(author.id)
    authors_page = open.click_authors()
    authors = authors_page.authors_of_the_store()
    for i in len(authors):
     authors = authors_page.author_name(i)
     assert authors != author.name


