import csv
import pandas
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)
#
#

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/ len(temp_list))
print(data["temp"].mean())
