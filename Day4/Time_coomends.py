import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop")
search_box.submit()
time.sleep(5)
laptop=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/h2/a')
laptop.click()
driver.quit()