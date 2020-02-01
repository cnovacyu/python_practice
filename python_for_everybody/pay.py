hrs = input("Enter Hours: ")
rate = input("Enter rate: ")

try:
        h = int(hrs)
        r = float(rate)
except:
        print("Invalid hours and rate, please enter correct values")
        quit()

def computepay(h,r):
        if h > 40:
                oth = h - 40
                otr = r * 1.5
                h = 40
                pay = (h * r) + (oth * otr)
        else:
                pay = h * r 
        return pay

p = computepay(h, r)
print(p)