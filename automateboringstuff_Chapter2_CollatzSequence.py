#check if number is even or odd and perform Collatz function, respectively 
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        print(3 * number + 1)
        return(3 * number + 1)

#prompt user to enter a number
#add in exception handling for non-integer values entered by user
print("Enter number: ")
try:
    num = int(input())
except ValueError:
    print("Please enter an integer.")
    
#assign value to the product of running the Collatz sequence the first time with user's prompted entry
nextnum = collatz(num)

#check if product is 1. If not, take each product and repeat the Collatz functions until 1 is returned
while nextnum != 1:
    nextnum = collatz(nextnum)
