import time
from selenium import webdriver

browser = webdriver.Chrome('D:/code/project/HFUT/chromedriver.exe')  # Optional argument, if not specified will search path.
time.sleep(5) # Let the user actually see something!
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()
time.sleep(5) # Let the user actually see something!
browser.quit()