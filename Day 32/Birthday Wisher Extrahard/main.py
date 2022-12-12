# ------------------------ Extra Hard Starting Project ------------------------------
import pandas
import datetime as dt
import random
import os
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "sivasatish780@gmail.com"
PASSWORD = 'qhvi rzwc tdyy bamn'

datetime = dt.datetime.now()
month = datetime.month
day = datetime.day

birthday_data = pandas.read_csv("birthdays.csv")
for (index, row) in birthday_data.iterrows():
    if row.month == month and row.day == day:
        email = row.email
        name = str(row["name"])
        # print(name)
        # print(email)
        random_file = random.choice(os.listdir("letter_templates"))
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace(PLACEHOLDER, name)

        # with open(file_path, mode="w") as completed_file:
        #     completed_file.write(new_letter)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.ehlo()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday\n\n{new_letter}")
