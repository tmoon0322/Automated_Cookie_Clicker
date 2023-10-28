from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(1)
english_button = driver.find_element(by="css selector", value="#langSelect-EN")
english_button.click()

time.sleep(1)
cookie_button = driver.find_element(by="css selector", value="#bigCookie")
click = True

delay_time = 10
def keep_clicking():
    timeout = time.time() + delay_time
    while click:
        if time.time() > timeout:
            break
        cookie_button.click()


def get_product():
    available_products = driver.find_elements(by="css selector", value=".storeSection .enabled")
    available_products_prices = driver.find_elements(by="css selector", value=".storeSection .enabled .content .price")
    num_list = driver.find_element(by="css selector", value="#cookies").text.split()[0].split(",")
    cookies = int("".join(num_list))
    available_products_prices.reverse()
    available_products.reverse()
    for product in available_products_prices:
        split_product = product.text.split()[0].split(",")
        product_price = int("".join(split_product))
        if product_price <= cookies:
            available_products[available_products_prices.index(product)].click()


def get_upgrade():
    available_upgrades = driver.find_elements(by="css selector", value="#store #upgrades .enabled")
    try:
        available_upgrades[0].click()
    except IndexError:
        pass







play = True
while play:
    keep_clicking()
    get_upgrade()
    get_product()
    delay_time += 1



















input("nice")






