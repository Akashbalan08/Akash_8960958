import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://indeed.ca')
time.sleep(3)

job_search = driver.find_element("id","text-input-what")
job_search.send_keys("part time")
time.sleep(2)

findjobs_button = driver.find_element(By.CLASS_NAME,"yosegi-InlineWhatWhere-primaryButton")
findjobs_button.click()
time.sleep(3)

Datesposted = driver.find_element(By.ID,"filter-dateposted")
Datesposted.click()
Date_Filter = driver.find_element(By.CSS_SELECTOR,".yosegi-FilterPill-dropdownListItemLink")
Date_Filter.click();
time.sleep(3)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

Job_type = driver.find_element(By.ID,"filter-remotejob")
Job_type.click()
Filter = driver.find_element(By.CSS_SELECTOR,".yosegi-FilterPill-dropdownListItemLink")
Filter.click()
time.sleep(3)

Job_radius = driver.find_element(By.ID,"filter-radius")
Job_radius.click()
radiusFilter = driver.find_element(By.CSS_SELECTOR,".yosegi-FilterPill-dropdownListItemLink")
radiusFilter.click()
time.sleep(3)

SignIn = driver.find_element(By.CSS_SELECTOR,".css-j2cyj")
SignIn.click()
time.sleep(3)




driver.quit()