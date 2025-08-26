from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com")
search=driver.find_element(By.NAME,"q")
print(search.is_displayed())
print(search.is_enabled())
driver.find_element(By.LINK_TEXT, "Register").click()
radio_male=driver.find_element(By.ID,"gender-male")
print(radio_male.is_selected())
radio_female=driver.find_element(By.ID,"gender-female")
print(radio_female.is_selected())
radio_male.click()
print(radio_male.is_selected())
print(radio_female.is_selected())
driver.quit()
