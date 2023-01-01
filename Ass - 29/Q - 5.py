"""Write a Python script to append list of city names in a
file ‘cities.txt’"""

import pickle

f=open("cities.txt","rb")
res=pickle.load(f)
f.close()
res.append("Agra")
f=open("cities.txt","wb")
pickle.dump(res,f)
f.close()