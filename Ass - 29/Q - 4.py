"""Write a Python script to store a list of city names in
a file ‘cities.txt’"""

import pickle

list=["Patna","Delhi","Mumbai","Sitamarhi"]
f=open("cities.txt","wb")
pickle.dump(list,f)
f.close()