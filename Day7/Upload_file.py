from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
file_input = driver.find_element(By.ID, "singleFileInput")
file_input.send_keys("C:\\Users\\Thinkpad\\Downloads\\Updated_Resume.pdf")
print("File uploaded successfully!")