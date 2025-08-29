from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(5)
alert.send_keys("Welcome")
#alert.accept()
alert.dismiss()