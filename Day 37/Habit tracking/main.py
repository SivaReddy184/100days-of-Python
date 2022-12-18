import requests
from datetime import datetime

today_date = datetime.now()
Date_frmt = today_date.strftime("%Y%m%d")
year = today_date.strftime("%Y%m")


USERNAME = "abc"
TOKEN = "anv"
# --------------------User Creation--------------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "anb",
    "username": "hhf",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ------------------------Creating Graph ---------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Reading Book graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# -------------------- Adding a pixel to graph ------------------------------

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
post_params = {
    "date": f'{year}{input("Enter the past or present date of this month to enter your entry : ")}',
    "quantity": input("enter the quantity: "),
}
response = requests.post(post_endpoint, json=post_params, headers=headers)
print(response.text)

# ----------------Update the pixel ------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{Date_frmt}"
update_params = {
    "quantity": "20",
}
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# ----------------Delete the pixel------------------------
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)

