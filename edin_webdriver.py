import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

import import_order_xls
'''
'''


def driver_init():
    # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    # binary = webdriver.FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    # driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    return driver


def wait_elem(driver, name_elem, by_attribute):
    elem = ''
    while not elem:
        try:
            elem = driver.find_element(by_attribute, name_elem)
        except:
            continue
    return elem


def send_text(driver, name_elem, value, by_attribute):
    elem = wait_elem(driver, name_elem, by_attribute)
    elem.send_keys(value)


def click_elem(driver, name_elem, by_attribute):
    elem = wait_elem(driver, name_elem, by_attribute)
    elem.click()


def login(driver):
    login_name = 'SonnihDistr'
    password = 'sonnihkojan11'
    driver.get('https://edo-v2.edi-n.com')# login page
    send_text(driver, "f_email", login_name, By.ID)
    send_text(driver, "f_password", password, By.ID)
    click_elem(driver, 'btn.btn-primary.block.full-width.m-b', By.CLASS_NAME)


def main(file):
    order_list = import_order_xls.read(file)
    if order_list:
        print('len(order_list)', len(order_list))
        driver = driver_init()
        login(driver)
        driver.get('https://edo-v2.edi-n.com/app/#/service/distr-retailer/chain/list/contractparties/0')
        driver.get('https://edo-v2.edi-n.com/app/#/service/distr-retailer/pricelist/42868')
        wait_elem(driver, "retailer_price_total", By.CLASS_NAME)
        table = driver.find_element_by_id("retailer_main_table")

        count = 0
        for row in table.find_elements_by_xpath(".//tr[@class='product-row']"):
            count += 1
            row_text = row.text
            barcode_search = row_text[:13]
            for item in order_list:
                if barcode_search == str(item['barcode']):
                    try:
                        row.find_elements_by_xpath(
                            ".//input[@class='ng-untouched ng-pristine ng-valid']"
                        )[1].send_keys(str(int(item['qtypack'])))
                    except Exception as e:
                        print(e)
        print('Script finish')
    else:
        print('order_list empty')


if __name__=="__main__":
    file = r'ВІММ-БІЛЛЬ-ДАНН заказник март21.xls'
    main(file)
