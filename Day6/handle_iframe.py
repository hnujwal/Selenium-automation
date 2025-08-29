from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()
driver.switch_to.frame("employeetable")
driver.find_element(By.ID,"nameInput").send_keys("ujwal")
driver.switch_to.default_content()
driver.switch_to.frame("registeruser")
driver.find_element(By.ID,"vfb-5").send_keys("ujwal")
driver.switch_to.default_content()

time.sleep(5)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe'))
driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/section/div/div/iframe'))
driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys("welcome")

time.sleep(5)   
driver.quit()
