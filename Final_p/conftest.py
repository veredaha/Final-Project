def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost/")
    parser.addoption("--framework", action="store", default="selenium_")
    parser.addoption("--browser_type", action="store", default="chrome")
    parser.addoption("--driver_path", action="store", default=r"C:\Users\vered\Desktop\chromedriver.exe")
    parser.addoption("--api_url", action="store", default="http://localhost:7017/api/")
    parser.addoption("--header", action="store", default={'accept': 'application/json'})

