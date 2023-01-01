"""Write a python script to add a finally block in question no 6 the above script"""
class Calculator:
    def __init__(self) -> None:
        try:
            self.num1=int(input("Enter 1st Number : "))
            self.num2=int(input("Enter 2nd Number : "))
        except ValueError:
            print("Please Enter Integer Only")
        finally:
            def add(self):
                print("sum =",self.num1+self.num2)

C=Calculator()
C.add()