import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(grey)
print(red)
print(black)

data_dict = {
    "Fur color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}
data_ = pandas.DataFrame(data_dict)
# data_.to_csv("squiral_data.csv")
print(data_)
