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
# from selenium import webdriver


# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')

def driver_init():
    # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    # binary = webdriver.FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    # driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    return driver

def login(driver):
    login = 'SonnihDistr'
    password = 'sonnihkojan11'
    driver.get('https://edo-v2.edi-n.com')# login page
    elem = driver.find_element_by_id("f_email")
    elem.send_keys(login)
    elem = driver.find_element_by_id("f_password")
    elem.send_keys(password)
    driver.find_element_by_class_name('btn.btn-primary.block.full-width.m-b').click()

def go_to_price_list(driver):
    driver.get('https://edo-v2.edi-n.com/app/#/service/distr-retailer/chain/list/contractparties/0')
    return driver.get('https://edo-v2.edi-n.com/app/#/service/distr-retailer/pricelist/42868')

# ищем таблицу

def main():
    driver = driver_init()
    login(driver)
    table_price_list = go_to_price_list(driver)
    table = table_price_list.find_element_('retailer_main_table')

    for row in table.find_elements_by_xpath(".//tr"):
        print(row.text)

if __name__=="__main__":
    main()