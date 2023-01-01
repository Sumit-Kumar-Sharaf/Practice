"""Write a Python script to extract book data from a bookfile
using pickle. Also print extracted book data"""

import pickle
f=open('bookfile.txt','rb')
res=pickle.load(f)
for key in res:
    print(key,res[key])
f.close()