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


def test_search_author_name(open)->None:
    mylogger.info("test for searching author name")
    results = open.search('Suzanne Collins')
    assert len(results) == 1

def test_search_book_name(open)->None:
    mylogger.info("test for searching book name")
    results = open.search('The Hunger Games')
    assert len(results) == 1

def test_search_empty(open)->None:
    mylogger.info("test for searching enpty input")
    results = open.search('')
    assert len(results) == 0