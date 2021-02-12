# randomly generate two lists of different sizes and return a list that contains 
# elements in both lists without duplicates.

import random

def generate_list():

    # determines how long the random list will be
    n = random.randint(1, 20)

    # samples numbers from 1 to 50 n times to create random list
    randomlist = random.sample(range(1,50), n)
    return(randomlist)


def list_overlap(list_x, list_y):

    print(f'List 1: {list_x}')
    print(f'List 2: {list_y}')

    # check common elements between both lists and remove dups
    overlap = list(set(x for x in list_x + list_y if x in list_x and x in list_y))
    overlap.sort()
    print(f'Elements in both lists are {overlap}')

a = generate_list()
b = generate_list()

list_overlap(a, b)