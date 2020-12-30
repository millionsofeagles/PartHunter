# PartHunter

### Selenium Bot to monitor and notify on availability of products.

##### Install:
The following packages are required dependencies:
- Firefox
- Geckodriver (Current Version of PartHunter Comes with exe for Windows)
- Python >3.8
- selenium
- Gmail Account

Edit the config.py file:

```SENDER_ADDRESS = "<sender gmail account>@gmail.com"
SENDER_PASSWORD = "<Password for sender gmail>"
RECIEVER_ADDRESSES = ["<List>", "<Of>", "<Reciever>", "<Addresses>"]
DRIVER_PATH = "<Path to the GeckoDriver executable>"
```

Add Items to the items.json file:
```
{
  "Items": [
    {
      "name": "PS5",
      "url": "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149",
      "msg_css_selector": ".add-to-cart-button",
      "price_css_selector": "Placeholder",
      "price": 500,
      "msg": "Add to Cart"
    },
    {
      "name": "Apple - MacBook Pro - 13\" Display with Touch Bar - Intel Core i5 - 8GB Memory - 256GB SSD - Silver",
      "url": "https://www.bestbuy.com/site/apple-macbook-pro-13-display-with-touch-bar-intel-core-i5-8gb-memory-256gb-ssd-silver/6287719.p?skuId=6287719&ref=212&loc=1&ref=212&loc=1&msclkid=9844e1999e0d1bac0a9dbe7502e7e5ae&gclid=CPKD8O2C9u0CFdj8swodI8cNkw&gclsrc=ds",
      "msg_css_selector": ".add-to-cart-button",
      "price_css_selector": "Placeholder",
      "price": 1500,
      "msg": "Add to Cart"
    },
    {
      "name": "NVIDIA GeForce RTX 3080 10GB GDDR6X PCI Express 4.0 Graphics Card - Titanium and Black",
      "url": "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",
      "msg_css_selector": ".add-to-cart-button",
      "price_css_selector": "Placeholder",
      "price": 800,
      "msg": "Add to Cart"
    }
  ]
}
```

##### Run the program
`user@hostname:~$ python3 watch.py`

##### Potential Errors
If you are using a gmail account for your SENDER_ADDRESS, you may encounter the following error:

```
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials k73sm28970392qke.63 - gsmtp')
```

If you do, click your user emblem in the top right of the page when in gmail, then click 'Manage your Google Account'.  On the left, click Security.  Scroll down to 'Less secure app access' and change it to on (not recommended for an everday account!). Now, try to run the program again.
