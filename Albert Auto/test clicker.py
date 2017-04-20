from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

##
##
##driver = webdriver.Chrome()
##driver.get("https://www.python.org")
##sleep(1)
##assert "Python" in driver.title
##elem = driver.find_element_by_name("q")
##elem.clear()
##elem.send_keys("pycon")
##elem.send_keys(Keys.RETURN)
##assert "No results found." not in driver.page_source
##driver.close()




driver = webdriver.Chrome()
driver.get("https://www.xkcd.com")
sleep(1)


for i in range(5):
    elem = driver.find_element_by_xpath('//*[@id="middleContainer"]/ul[1]/li[3]/a')
    elem.click()
    sleep(1)

driver.quit()
