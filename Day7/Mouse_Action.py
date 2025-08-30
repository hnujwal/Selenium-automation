import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://vinothqaacademy.com/mouse-event/")
driver.implicitly_wait(5)
first=driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[8]/a")
second=driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[8]/ul/li[2]/a")
third=driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[8]/ul/li[2]/ul/li[1]/a")
action=ActionChains(driver)
action.move_to_element(first).move_to_element(second).move_to_element(third).click().perform()# perform mouse hover action
time.sleep(5)
driver.back()
driver.refresh()
source=driver.find_element(By.XPATH,'//*[@id="draggableElement"]')
destination=driver.find_element(By.XPATH, '//*[@id="droppableElement"]')
action.drag_and_drop(source,destination).perform()# perform drag and drop
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#scroll down
time.sleep(3)
action.double_click(driver.find_element(By.XPATH, "//*[@id='dblclick']")).perform()# double click
action.context_click(driver.find_element(By.XPATH,'//*[@id="rightclick"]')).perform()# right click
time.sleep(3)
driver.quit()
