from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")#admin:admin@ is the authentication part