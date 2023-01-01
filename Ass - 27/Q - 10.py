"""Write a python script to implemented a nested Try Except block"""

def studentDetail():
    name=input("Enter your name: ")
    try:
        if name.isalpha()==False:
            raise ValueError
        try:
            Class=int(input("Enter Your class: "))
            try:
                age=int(input("Enter your age: "))
            except ValueError:
                print("Age Must Be Integer Value")
        except ValueError:
            print("Class Must Be Integer Value")
    except ValueError:
            print("Name Must Conatin Alphabets Only")

studentDetail()
