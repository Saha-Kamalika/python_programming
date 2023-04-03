s="Hello, I am Kamalika Saha"
#writing to a file
with open("kam.txt","w") as k:  #using context manager no need to close the file
    k.write(s)

f=open("kam.txt","w")
f.write("I am an ECE undergrad")    #new file created
f.close()

#reading a file
rd=open("kam.txt","r")
st=rd.read()
print(st)
rd.close()   #closing the file is mandatory here