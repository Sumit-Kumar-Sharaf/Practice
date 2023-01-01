"""Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file"""

f=open("demo1.txt","w")
if f.mode=="r":
    print("Yes, File Is Read Only")
else:
    print("No, The File Is Not Read Only")
print(f.closed)
print(f.mode)
print(f.name)
f.close()
print(f.closed)

