'''spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it.'''

#creating a function to loop through a list, except for the last value. Also adds 
#a comma and space after each item in the list.
def repeatlist(items):
    for item in range(len(items) - 1):
        print((items[item]), end=', ')

    #Print 'and' and the last item in the list
    print('and ' + items[-1])

spam = ['apples', 'bananas', 'tofu', 'cats', 'monsters', 'bubbles', 'rugrats']
repeatlist(spam)
