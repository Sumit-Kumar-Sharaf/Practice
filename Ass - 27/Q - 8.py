"""Write a python script to implement try except and else block for division"""
def divide():
    try:
        num1=int(input("Enter 1st Number: "))
        num2=int(input("Enter 2nd Number: "))
        result=num1/num2
    except ValueError:
        print("Please Enter Integer Only")
    except ZeroDivisionError:
        print("Denominator Can't Be Zero")
    else:
        print(result)

divide()