import time
import sys
from selenium import webdriver

if len(sys.argv) < 2:
    print 'Missed argument needful. Please try "python login.py fully_server_URL"'
    sys.exit()


testurl = sys.argv[1]

driver = webdriver.Chrome()
driver.get(testurl)

element = driver.find_element_by_name("user");
element.send_keys("admin");

element = driver.find_element_by_name("pass");
element.send_keys("admin");

submit_button = driver.find_elements_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr[4]/td[3]/input')[0]

submit_button.click();

time.sleep(5)
driver.close()
