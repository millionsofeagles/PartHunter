import smtplib
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config
import json
import time
from pathlib import Path #python 3.4+ for support

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
    '''
    Reads the config.py file to send found items to a list of user's email addresses.
    '''
    sender_address = config.SENDER_ADDRESS
    receiver_address = dest_address
    account_password = config.SENDER_PASSWORD
    subject = "ITEM FOUND: " + item.name
    #python 3.5+ for f string support
    body = f"A {item.name} has been found for less than {str(item.price)} at: \n\n {item.url}"

    # Endpoint for the SMTP Gmail server (Don't change this!)
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login with your Gmail account using SMTP
    smtp_server.login(sender_address, account_password)
    message = f": {subject} Subject\n\n {body}"
    smtp_server.sendmail(sender_address, receiver_address, message)
    smtp_server.close()

def search(Items):
    '''
    Searches for each item from the Items list.
    '''
    for item in Items:
        options = Options()
        options.add_argument("--headless")
        driver_path = Path(__file__).parent / "geckodriver.exe"
        driver = webdriver.Firefox(executable_path=driver_path, options=options, firefox_profile=config.FF_PROFILE_PATH)
        driver.get(item.url)
        try:
            msg_elem = driver.find_element_by_css_selector(item.msg_css_selector)
            print(f"\t{item.name} found.")
            #price_elem = driver.find_element_by_css_selector(item.price_css_selector)
            if item.msg in msg_elem.text:# and int(price_elem.text) <= item.price:
                for dest_address in config.RECIEVER_ADDRESSES:
                    send_mail(item, dest_address)
                if item.add_to_cart == True:
                    element = driver.find_elements_by_class_name("add-to-cart-button")
                    element[0].click()
                    time.sleep(5)
        except:
            print(f"\t{item.name} not found.")
        time.sleep(2) # 2 second wait between the end of one request and the beginning of the next
        driver.quit()

def populate_items():
    '''
    Reads the items.json file and returns an Item object for each.
    '''
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
    items = populate_items()
    count = 0
    while True:
        print(f"Starting Search number: {count}")
        search(items)
        count += 1
