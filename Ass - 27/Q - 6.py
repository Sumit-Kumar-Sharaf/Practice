"""Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions"""

class Calculator:
    def add(self):
        try:
            self.num1=int(input("Enter 1st Number : "))
            self.num2=int(input("Enter 2nd Number : "))
            print("Sum =",self.num1+self.num2)
        except ValueError:
            print("Please Enter Integer Only")
    def substract(self):
        try:
            self.num1=int(input("Enter 1st Number : "))
            self.num2=int(input("Enter 2nd Number : "))
            print("Difference =",self.num1-self.num2)
        except ValueError:
            print("Please Enter Integer Only")
    def multiply(self):
        try:
            self.num1=int(input("Enter 1st Number : "))
            self.num2=int(input("Enter 2nd Number : "))
            print("Product =",self.num1*self.num2)
        except ValueError:
            print("Please Enter Integer Only")
    def divide(self):
        try:
            self.num1=int(input("Enter 1st Number : "))
            self.num2=int(input("Enter 2nd Number : "))
            print("Quotient =",self.num1/self.num2)
        except ValueError:
            print("Please Enter Integer Only")
        except ZeroDivisionError:
            print("Denominator Can't Be Zero")
    
C1=Calculator()
C1.add()
C1.substract()
C1.multiply()
C1.divide()