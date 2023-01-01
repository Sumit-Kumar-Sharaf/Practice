"""Write a python script to handle the ArithmeticError"""

try:
    def divide(x,y):
        print(x/y)
except ArithmeticError:
    print("Denominator Can't Be zero")

divide(10,0)