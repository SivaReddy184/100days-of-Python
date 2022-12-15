import requests
from twilio.rest import Client

account_sid = "ACbf895611d14f60019071fea7302c341b"
auth_token = "25b504d0d103ee0903bfe58edad6a3b4"

API_KEY = "b7bb7217c7734bcb9f140345221512"
LAT = 0.507068
LONG = 101.447777

response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={LAT},{LONG}&days=1")
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
# print(weather_data["forecast"]["forecastday"][0]["hour"][10]["chance_of_rain"])

hourly_data_slice = weather_data["forecast"]["forecastday"][0]["hour"][7:19]
print(hourly_data_slice)
# print(hourly_data[10]["chance_of_rain"])

will_rain = False
for hour in hourly_data_slice:
    chance = hour["chance_of_rain"]
    if chance > 0:
        will_rain = True
        # print("It's going to rain today")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+19259404526",
        to="+1432022"
    )
    print(message.status)


# # Python Environment Variables:
#
# Environment variables are nothing but secret variables. When we don't want to expose our personal keys like API
# key, email password in our code we can assign them as environment variables.
#
# ### In shell-
#
#     export MY_EMAIL_PSWRD=Agf1873@
#
#   Hit ‘’env” command to check current env variables in shell
#
# ### In code -
#
#       Import os
#
#       My_pswrd = os.environ.get(”MY_EMAIL_PSWRD”)
