import time
import sys
from selenium import webdriver

# Use arguments to get parameters.
#if len(sys.argv) < 2:
#    print 'Missed argument needful. Please try "python login.py fully_server_URL account password"'
#    sys.exit()

#testurl = sys.argv[1]
#account = sys.argv[2]
#password = sys.argv[3]

with open("parameters.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip('\n'))


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(array[0])

element = driver.find_element_by_name("user");
element.send_keys(array[1]);

element = driver.find_element_by_name("pass");
element.send_keys(array[2]);

submit_button = driver.find_elements_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr[4]/td[3]/input')[0]

submit_button.click();

time.sleep(5)
driver.close()
