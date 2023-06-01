import timeit

def create_pairs():
    output = []
    for a in (1, 3, 5, 7, 9, 11):
        for b in (2, 4, 6, 8, 10, 12):
            output.append((a, b))
    return output

def create_pairs_comprehension():
    return [(a, b) for a in (1, 3, 5, 7, 9, 11) for b in (2, 4, 6, 8, 10, 12)]
  
RANGE = 10_000
LIST = [element for element in range(RANGE)]  
SET = {element for element in range(RANGE)}
def list_find(ele):
    return ele in LIST

def set_find(ele):
    return ele in SET

# Creating a SET typically takes over twice the time:
# ls="ls = list(range(100_000))"
# ss="ss = set(range(100_000))"

# t1 = timeit.timeit(ls, number=1000)
# t2 = timeit.timeit(ss, number=1000)
# print("Time taken by list_find():", t1, "milliseconds")
# print("Time taken by set_find():", t2, "milliseconds")

my_list =list(range(100_000))
my_set =set(range(100_000))
list_time = timeit.timeit("99_999 in my_list", number=1000, globals=globals())
set_time = timeit.timeit("99_999 in my_set", number=1000, globals=globals())
print(f'Time taken by list find: {list_time:.6f} milliseconds')
print(f'Time taken by set find: {set_time:.6f} milliseconds')
# This is an impressive difference!

# t1 = timeit.Timer(lambda: list_find(9999))
# print("Time taken by list_find():", t1.timeit(number=100000), "milliseconds")
# t2 = timeit.Timer(lambda: set_find(9999))
# print("Time taken by set_find():", t2.timeit(number=100000), "milliseconds")


# # Time create_pairs() function
# t1 = timeit.Timer(lambda: create_pairs())
# print("Time taken by create_pairs():", t1.timeit(number=100000), "milliseconds")

# # Time create_pairs_comprehension() function
# t2 = timeit.Timer(lambda: create_pairs_comprehension())
# print("Time taken by create_pairs_comprehension():", t2.timeit(number=100000), "milliseconds")
