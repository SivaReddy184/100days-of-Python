import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# ----------------------------------------- GETTING PRODUCT PRICE --------------------------------------------------

amazon_endpoint = "https://www.amazon.in/dp/B0819ZZK5K/?coliid=I36S93GQHW1XJC&colid=1MV2WGARB599U&ref_=gv_ov_lig_pi_dp&th=1"
headers = {'Accept-Language': "en-US,en;q=0.9",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/108.0.0.0 Safari/537.36 "
           }
response = requests.get(amazon_endpoint, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find("span", class_="a-price-whole")
title = soup.find(id="productTitle")

# ----IF PRICE IS < 1000 ---------
try:
    amazon_price = float(price.text)
    print(amazon_price)
# ----IF PRICE IS > 1000 ---------
except ValueError:
    amazon_price = float(price.text.split(".")[0].split(",")[0] + price.text.split(".")[0].split(",")[1])
    print(amazon_price)

# -----------------------------------SENDING EMAIL WHEN THE PRICE IS BELOW TARGET PRICE -------------------------

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO = os.environ["TO"]
TARGET_PRICE = 1130

if amazon_price < TARGET_PRICE:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.ehlo()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO,
                            msg=f"Subject:Amazon Price Alert Reminder\n\nHey! {title.text.strip()} is now Rs.{amazon_price}."
                                f" Buy here quickly {amazon_endpoint}")
