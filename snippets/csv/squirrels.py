import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


grays = data[data['Primary Fur Color'] == "Gray"]
blacks = data[data['Primary Fur Color'] == "Black"]
reds = data[data['Primary Fur Color'] == "Cinnamon"]
print(len(grays))
print(len(blacks))
print(len(reds))

data_dict = {
  "Fur Color": ['Gray', 'Black', 'Red'],
  "Count": [2473,103,392]
}

df=pandas.DataFrame(data_dict)
df.to_csv('sq.csv')