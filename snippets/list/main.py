# numbers = [1,2,3,4]

# def sqr(n):
#   return n**2
# def is_pair(n):
#   return n%2==0

# sqrs = [sqr(number) for number in numbers]
# print(sqrs)

# dbl = [n*2 for n in numbers if is_pair(n)]
# print(dbl)




list1= ["a", '1','2']
list2 = list(map(lambda s: "fixed_string" + s, list1))
ran = range(len(list1))
print(ran)


