"""Write a python script to handle multiple Exception in one try"""

try:
        x=int(input("Enter 1st Number : "))
        y=int(input("Enter 2nd Number : "))
        print(x/y)
except ZeroDivisionError:
    print("Denominator Cant't Be Zero")
except ValueError:
    print("Please Enter Integer Only")

