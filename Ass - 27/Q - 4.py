"""Write a python script to handle a ValueError"""
try:
    l=[2,5,1,1,9,8]
    l.remove(0)
    print("Removed")
except ValueError:
    print("Value Doesn't Exist")

