# with open("weather_data.csv") as weather:
#     data = weather.readlines()

# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
# avg = sum(temp_list)/len(temp_list)
# print(avg)
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data.condition)
print(data["condition"])

# get data from rows (hold a column and equal it to any row data to return row)
print(data[data.day == "Monday"])

# maximum temperature day
print(data[data.temp == data["temp"].max()])


# accessing a row data
monday = data[data.day == "Monday"]
print(monday.temp)


# creating a dataframe from scratch
data_dict = {
    "students": ["siva", "sathi", "tim"],
    "scores": [76, 54, 33]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)

# converting data to csv file
new_data.to_csv("new_data.csv")