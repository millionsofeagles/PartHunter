import smtplib
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config
import json
import time

class Item:
    def __init__(self, name, url, msg_css_selector, price_css_selector, msg, add_to_cart, price=0):
        self.name = name
        self.url = url
        self.msg_css_selector = msg_css_selector
        self.price_css_selector = price_css_selector
        self.msg = msg
        self.add_to_cart = add_to_cart
        self.price = price

def send_mail(item, dest_address):

    sender_address = config.SENDER_ADDRESS
    receiver_address = dest_address
    account_password = config.SENDER_PASSWORD
    subject = "ITEM FOUND: " + item.name
    body = "A " + item.name + \
           " has been found at: \n\n" + \
           item.url + \
           "\n\nfor less than $" + \
           str(item.price)

    # Endpoint for the SMTP Gmail server (Don't change this!)
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login with your Gmail account using SMTP
    smtp_server.login(sender_address, account_password)
    message = "Subject: " + subject + "\n\n" + body
    smtp_server.sendmail(sender_address, receiver_address, message)
    smtp_server.close()

def search(Items):
    for item in Items:
        #TODO: Use an relative path for geckodriver
        options = Options()
        options.add_argument("--headless")
        driver_path = config.DRIVER_PATH
        driver = webdriver.Firefox(executable_path=driver_path, options=options, firefox_profile=config.FF_PROFILE_PATH)
        driver.get(item.url)
        msg_elem = driver.find_element_by_css_selector(item.msg_css_selector)
        #price_elem = driver.find_element_by_css_selector(item.price_css_selector)
        if item.msg in msg_elem.text:# and int(price_elem.text) <= item.price:
            for dest_address in config.RECIEVER_ADDRESSES:
                send_mail(item, dest_address)
            if item.add_to_cart == True:
                element = driver.find_elements_by_class_name("add-to-cart-button")
                element[0].click()
                time.sleep(5)
        driver.close()
    driver.quit()

def populate_items():
    jsonfile = open("items.json", )
    items = []
    data = json.load(jsonfile)
    for entry in data['Items']:
        items.append(Item(
            entry["name"],
            entry["url"],
            entry["msg_css_selector"],
            entry["price_css_selector"],
            entry["msg"],
            entry["add_to_cart"],
            entry["price"],
        ))
    return items

if __name__ == '__main__':
    #TODO: Loop this indefinitely
    #TODO: Add waits to web requests
    items = populate_items()
    search(items)
