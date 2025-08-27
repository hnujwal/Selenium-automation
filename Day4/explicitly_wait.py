from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait=WebDriverWait(driver,10)#declaration of explicit wait
username=wait.until(EC.visibility_of_element_located((By.NAME,"username")))#use explicit wait
password=wait.until(EC.visibility_of_element_located((By.NAME,"password")))
username.send_keys("Admin")
password.send_keys("admin123")
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.quit()    
