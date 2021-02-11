# ask the user for a number to check and a number to divide by. 
# Print out an appropriate message whether the number is even or odd
# Check if the number is a multiple of 4. Check if the number
# evenly divides.

def odd_even():
    num = int(input('Enter a number to check: '))
    check = int(input('Enter a number to divide by: '))

    if num % 4 == 0:
        print(f'{num} is a multiple of 4')
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')

    if num % check == 0:
        print(f'{num} evenly divides by {check}')
    else:
        print(f'{num} does not evenly divide by {check}')

odd_even()