from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# ----------------------------------UPDATING SHEET WITH IATA CODES --------------------------------------------
# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}
# ------------------------------------CHECKING FLIGHT PRICES AND SENDING SMS ---------------------------------------
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = "LON"
for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"],
                                         from_time=tomorrow,
                                         to_time=six_month_from_today
                                         )
    if flight is None:
        continue
    if flight.price < destinations[destination_code]["price"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                    f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}. "
        )
