# Print out all the elements of a list that are less than number specified by an user

def list_less_than(num_list):

    num = int(input("Enter a number: "))

    b = [x for x in num_list if x < num]
    print(f'Items in the list that are less than {num} are: {b}')

# sample list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_less_than(a)