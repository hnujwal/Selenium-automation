from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://orangehrm.com")
print(driver.title) # Get the title of the current page
print(driver.current_url) # Get the current URL of the page
#print(driver.page_source) # Get the page source of the current page
driver.quit() # Quit the browser and end the session
