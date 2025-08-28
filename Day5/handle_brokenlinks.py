import requests as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()    
alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0
for link in alllinks:
    url=link.get_attribute("href")
    try:
        res=req.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"is a broken link")
        count+=1
    else:
        print(url,"is a valid link")
print("Total number of broken links are:",count)            