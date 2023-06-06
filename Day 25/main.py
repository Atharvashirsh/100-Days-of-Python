# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# Calculating Average temperature
# avg = round(sum(temp_list) / len(temp_list), 2)
# print(avg)

# print(data["temp"].mean())

# Maximum value
# print(data["temp"].max())

# Row data for max temp
# print(data[data.temp == data["temp"].max()])

# Monday data
# monday = data[data.day == "Monday"]
# print(monday)

# monday temp to fahrenheit
# f_temp = (9 * monday.temp) / 5 + 32
# print(f_temp)

# Creating a dataframe
data_dict = {
    "students": ["Atharva", "Max", "Avantika"],
    "scores": [76, 56, 81],
}

# print(data_dict)
data = pandas.DataFrame(data=data_dict)
print(data)
data.to_csv("new_data.csv")
