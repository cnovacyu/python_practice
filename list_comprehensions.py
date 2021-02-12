# write one line that takes a list and makes a new list that only contains even elements

def list_comprehensions(num_list):

    evens_only = [x for x in num_list if x % 2 == 0]
    print(evens_only)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list_comprehensions(a)