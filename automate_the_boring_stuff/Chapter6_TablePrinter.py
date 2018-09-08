def printTable(items):
    max_len = 0
    x = 0 
    len_str = [[] for item in range(len(items))] 

    #determine the maximum number of items in each row of the lists input
    #use the max number found as the variable for looping through each col in each row
    for row in items:
        if len(row) > max_len:
            max_len = len(row)
    
    #calculate the len of each string. Store the len of each string in 
    #a separate list for each row
    for row in range(0, len(items)):
        for column in range(0, max_len): 
            length = len(items[row][column])
            len_str[x].append(length)
        x += 1

    #use for debugging. Should print a list of len of each string 
    # per row of the lists input
    #print(len_str)

    #find the max of each row's string length and override the list
    #to only hold the max str lengths for each row
    for row in range(len(len_str)):
        max_str = max(len_str[row]) + 1
        len_str[row] = max_str

    #use for debugging. Should only have one max value per row of lists inputt            
    #print(len_str)

    x = 0

    #print each row in a column (1st item on top, 2nd item underneath, etc)
    #will right justify each item based on the row the string is in
    for column in range(0, max_len):
        for row in range(0, len(items)):
            print(items[row][column].rjust(len_str[x]), end='')
            x += 1
        x = 0    
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)