from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.awwwards.com/websites/scrolling/")
#driver.execute_script("window.scrollBy(0, 1000)")#scroll down upto 1000px
find=driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div/ul/li[23]/div/figure/a/img")
#driver.execute_script("arguments[0].scrollIntoView();",find)#scroll down until the element is in view

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#scroll down to bottom
