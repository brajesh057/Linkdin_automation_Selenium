from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from _datetime import datetime
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://www.linkedin.com/jobs/search/?keywords=Automation&location=Bangalore%20Urban%2C%20Karnataka%2C%2"
               "0India&locationId=&geoId=112376381&f_TPR=r86400&position=1&pageNum=0")
time.sleep(5)
sign_in = driver.find_element(By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
time.sleep(2)
email_id = driver.find_element(By.XPATH, value='//*[@id="username"]')
email_id.send_keys("brijeshnaik01@gmail.com", Keys.ENTER)
password = driver.find_element(By.XPATH,value='//*[@id="password"]')
password.send_keys("Br@jeshn@ik057")
send_button = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
send_button.click()
time.sleep(2)

#listing all the jobs

listing = driver.find_elements(By.CLASS_NAME, 'ember-view.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item')
# going through all jobs
for list1 in range(len(listing)):

    if 'Easy Apply' in listing[list1].text:
        listing[list1].click()
        time.sleep(3)
    else:
        pass
