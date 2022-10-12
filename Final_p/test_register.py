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
from models.ApiUserDto import ApiUserDto
from apis.account import accountApi
import time


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()



def test_register_valid(open)->None:
    mylogger.info("test for registering with valis details")
    home_page = open.register('admin@sela.co.il', '123456', 'Vered','Aharonov')
    #bug register button doesn't work

def test_register_empty_email(open)->None:
    mylogger.info("test for registering with empty email")
    home_page = open.register('', '123456', 'Vered','Aharonov')
    #bug register button doesn't work

def test_register_invalid_email(open)->None:
    mylogger.info("test for registering with invalid email")
    home_page = open.register('admin', '123456', 'Vered','Aharonov')
    #bug register button doesn't work

def test_register_empty_passwd(open)->None:
    mylogger.info("test for registering with empty password")
    home_page = open.register('admin@sela.co.il', '', 'Vered','Aharonov')
    #bug register button doesn't work

def test_register_invalid_passwd(open)->None:
    mylogger.info("test for registering with invalid password")
    home_page = open.register('admin@sela.co.il', '123', 'Vered','Aharonov')
    #bug register button doesn't work

def test_register_empty_firstname(open)->None:
    mylogger.info("test for registering with empty firstname")
    home_page = open.register('admin@sela.co.il', '123456', '','Aharonov')
    #bug register button doesn't work

def test_register_empty_lastname(open)->None:
    mylogger.info("test for registering with empty lastname")
    home_page = open.register('admin@sela.co.il', '123456', 'Vered','')
    #bug register button doesn't work

def test_register_with_registered_email(open)->None:
    mylogger.info("test for registering with already registered email")
    home_page = open.register('admin@sela.co.il', '123456', 'Vered','Aharonov')
    home_page = open.register('admin@sela.co.il', '123456', 'Vered', 'Aharonov')
    #bug register button doesn't work

def test_register_api(resgister_account,login_vv, accountapi : accountApi)->None:
 """
 test for posting account
 """
 mylogger.info("test for posting account")
 accountapi.post_account(resgister_account)
 res = accountapi.post_login(login_vv)
 ref = accountapi.post_refreshtoken(login_vv)
 assert res.userId == ref.userId














