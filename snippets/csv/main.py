# import csv

# with open("data.csv") as df:
#   # data = df.readlines()
#   data = csv.reader(df)
#   for row in data[1:]:
#     print(row)

import pandas

# data = pandas.read_csv('data.csv')
# print(data)
# print(data["temp"])
# print(data["condition"])

# temp_list =  data["temp"].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.condition)
# print(data['condition'])

# data_dict = data.to_dict()
# print(data_dict)

# print(data[data.day == 'Monday'])
# print(data[data['day'] == 'Tuesday'])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp > 22])

# Creating DataFrame data-dictionary -> dataFrame
data_dict={
  "students": ["Amy", "James", "Angela"],
  "scores": [76,56,65]  
}

df = pandas.DataFrame(data_dict)
# df.to_csv('new_file.csv')
print(df)

list = [ row.students for index,row in df.iterrows()]
print(list)