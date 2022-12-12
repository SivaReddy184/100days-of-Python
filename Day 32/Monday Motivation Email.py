# ANGELA METHOD with modification of SMTP_SSl instead of SMTP and .ehlo instead of starttcl with addition of port number
import datetime as dt
import smtplib
import random

MY_EMAIL = "sivasatish780@gmail.com"
PASSWORD = 'qhvi rzwc tdyy bamn'
SENDERS_EMAIL = 'sivatestqa@gmail.com'

with open("quotes.txt", "r") as file:
    quotes_list = file.readlines()
    random_quote = random.choice(quotes_list)
    print(random_quote)

datetime = dt.datetime.now()
weekday = datetime.weekday()

if weekday == 0:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.ehlo()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=SENDERS_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")


