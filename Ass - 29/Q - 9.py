"""Write a Python script to store book data in a file. Book data
is in the form of a dictionary in which book name is the key and
price is its value. Use pickle to store data into a file
(say bookfile)"""

import pickle

book_detail={'Python':200,'Java':250,'JavaScript':280,'C++':180}
f=open('bookfile.txt','wb')
pickle.dump(book_detail,f)
f.close()