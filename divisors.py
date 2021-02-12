# ask the user for a number and then print out all the divisors of that number

def divisors():
    num = int(input('Enter a number: '))

    b = [x for x in range(1, num+1) if num % x == 0]
    print(f'The divisors for {num} are {b}')

divisors()