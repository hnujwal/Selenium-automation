from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.amazon.com/")
driver.get("https://www.flipkart.com/")
driver.maximize_window() # Maximize the browser window
driver.back()
driver.forward()
driver.refresh()
driver.quit() # Quit the browser and end the session