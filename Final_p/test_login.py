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

def test_login_valid(open)->None:
    mylogger.info("test for logging in with valid details")
    store_page = open.login('admin@sela.co.il','123456')
    assert 'Welcome to our store' in store_page.check_page_valid()

def test_login_empty_email(open)->None:
    mylogger.info("test for logging in with empty email")
    home_page = open.login('','123456')
    #No alert message to assert

def test_login_invalid_email(open)->None:
    mylogger.info("test for logging in with invalid email")
    home_page = open.login('admin.co.il','123456')
    #No alert message to assert

def test_login_invalid_passwd(open)->None:
    mylogger.info("test for logging in with invalid password")
    home_page = open.login('admin@sela.co.il','123')
    #No alert message to assert

def test_login_empty_passwd(open)->None:
    mylogger.info("test for logging in with empty password")
    home_page = open.login('admin@sela.co.il','')
    #No alert message to assert

def test_login_unregistered_email(open)->None:
    mylogger.info("test for logging in with unregistered email")
    home_page = open.login('veredaha@sela.co.il','123456')
    #No alert message to assert








