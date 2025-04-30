def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b

print("Write 1 for add, 2 for subtraction, 3 for multiplication,4 for division")
ch=int(input("Enter your choice:"))
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
if ch==1:
    print("Sum=", add(n1,n2))
elif ch==2:
    print("Sub=", sub(n1,n2))
elif ch==3:
    print("Multi=", multi(n1,n2))
elif ch==4:
    print("Divi=", divi(n1,n2))