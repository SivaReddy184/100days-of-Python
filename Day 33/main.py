import requests
from datetime import *
import smtplib
import time

MY_EMAIL = "abc@gmail.com"
PASSWORD = 'abc'

MY_LAT = 14.558208047932865
MY_LONG = 79.34277387122837


# -------------------------------ISS POSITION -------------------------------------------------------
def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_position_ = (iss_latitude, iss_longitude)
    # print(iss_position_)
    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# -------------------------------SUNRISE & SUNSET TIME --------------------------------------------------

def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = int(datetime.now().hour)
    # print(data)
    if time_now >= sunset or time_now <= sunrise:
        return True


# --------------------------------------WHEN ISS IS NEAR ME ---------------------------------

# if iss is near me and also my time is night then I will get the email to look up on sky
while True:
    time.sleep(60)
    if iss_position() and is_night():
        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.ehlo()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look UP\n\nThe ISS is above you in the SKY")
            print("Email Sent")
