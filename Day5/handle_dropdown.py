from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://practice.expandtesting.com/dropdown")
driver.maximize_window()
dropdown=Select(driver.find_element(By.ID,"country"))
dropdown.select_by_visible_text("India")
#dropdown.select_by_value("IN")
#dropdown.select_by_index(13)
all_options=dropdown.options
print("total number of options:", len(all_options))
for option in all_options:
    print(option.text)