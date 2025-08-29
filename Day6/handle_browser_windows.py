from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
windows_id=driver.window_handles
#print(windows_id)
#print(driver.title)
#driver.switch_to.window(windows_id[1])
for win_id in windows_id:
    driver.switch_to.window(win_id)
    print(driver.title)
driver.quit()