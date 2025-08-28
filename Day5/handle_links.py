from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Books").click()
# get all link texts
tags=driver.find_elements(By.TAG_NAME,"a")
for tag in tags:
    print(tag.text)
driver.quit()    