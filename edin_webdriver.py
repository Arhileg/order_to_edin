import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

'''
'''

def driver_init():
    # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    # binary = webdriver.FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    # driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    return driver

def login(driver):
    login = 'SonnihDistr'
    password = 'sonnihkojan11'
    driver.get('https://edo-v2.edi-n.com')# login page
    driver.implicitly_wait(7)
    elem = driver.find_element_by_id("f_email")
    time.sleep(0.1)
    elem.send_keys(login)
    elem = driver.find_element_by_id("f_password")
    time.sleep(0.1)
    elem.send_keys(password)
    time.sleep(0.1)
    driver.find_element_by_class_name('btn.btn-primary.block.full-width.m-b').click()

def main():
    driver = driver_init()
    login(driver)
    driver.get('https://edo-v2.edi-n.com/app/#/service/distr-retailer/chain/list/contractparties/0')
    driver.get('https://edo-v2.edi-n.com/app/#/service/distr-retailer/pricelist/42868')
    driver.implicitly_wait(10)
    table = driver.find_element_by_id("retailer_main_table")

    count = 0
    for row in table.find_elements_by_xpath(".//tr[@class='product-row']"):
        count += 1
        print(row.text)
        if row.text.find('4823061320339')>-1:
            # driver.switch_to.frame(
            try:
                row.find_elements_by_xpath(".//input[@class='ng-untouched ng-pristine ng-valid']")[1].send_keys("2")
            except Exception as e:
                print(e)

        print(row.text.find('4823061320339'))
        # print(row.tag_name)
        if count>30:
            break


if __name__=="__main__":
    main()