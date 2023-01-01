"""Write a Python script to search whether a particular city
is there in the file ‘cities.txt’ or not"""

import pickle

def search(word):
    f=open('cities.txt','rb')
    res=pickle.load(f)
    if word in res:
        print("%s Exist In The List"%word)
    else:
        print("%s Doesn't Exist In The List"%word)
    f.close()

search("Mumbai")