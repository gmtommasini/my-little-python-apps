my_dict ={}
my_dict['name'] = "John"
my_dict['age'] = 24

other_dict = {
  'add': ' some add',
  'date': '2023/12/13'
}
# my_dict['additional'] = other_dict
my_dict.update(other_dict)
for y in my_dict:
  print()

# list = [ y for x,y in my_dict.items() ] 
# print(my_dict)
# print(list)
