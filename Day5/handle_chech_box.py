from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
check_box=driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day")]')
print(len(check_box))
# Click all checkboxes
for i in range(len(check_box)):
    check_box[i].click()
# check that checkboxes are selected if selected deselect them
for checkbox in check_box:
    if checkbox.is_selected():
        checkbox.click()