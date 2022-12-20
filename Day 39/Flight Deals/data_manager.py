import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
AUTH_USERNAME = os.environ["AUTH_USERNAME"]
AUTH_PASSWORD = os.environ["AUTH_PASSWORD"]
sheety_endpoint = "https://api.sheety.co/f675a0980916bc8e961bb4b42be69215/flightDeals/prices"


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(sheety_endpoint, auth=(AUTH_USERNAME, AUTH_PASSWORD))
        self.destination_data = sheet_response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, auth=(AUTH_USERNAME, AUTH_PASSWORD))
            print(response.text)
