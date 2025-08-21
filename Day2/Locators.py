from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com")
driver.maximize_window() # Maximize the browser window
driver.find_element(By.NAME,"q").send_keys("laptop")
driver.find_element(By.ID,"small-searchterms").clear() # Clear the search box
driver.find_element(By.LINK_TEXT,"Register").click() # Click on the Register link
link=driver.find_elements(By.TAG_NAME,"a") # Find all anchor tags
print(len(link)) # Print the number of anchor tags found
driver.close() # Close the browser window