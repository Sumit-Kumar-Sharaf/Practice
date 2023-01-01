"""Write a Python script to count the number of Python keywords
occurring in a python source file"""

#Not Complete
import pickle
import keyword
keyword_list=keyword.kwlist
f=open('pyfile.txt','r')
for line in f.readlines():
    list=line.split(" ")
    print(list)
    for word in line:
        if word in keyword_list:
            print(word)

