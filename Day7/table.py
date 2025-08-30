from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.w3.org/WAI/UA/2002/06/thead-test")
driver.maximize_window()
row1 = len(driver.find_elements(By.XPATH, "/html/body/table[1]/tbody/tr[1]/td"))
for r in range(1, row1 + 1):
    col1 = len(driver.find_elements(By.XPATH, f"/html/body/table[1]/tbody/tr[{r}]/td"))
    for c in range(1, col1 + 1):
        print(driver.find_element(By.XPATH, f"/html/body/table[1]/tbody/tr[{r}]/td[{c}]").text, end=" | ")
    print()
driver.quit()