a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
min=0
if a>=b and c>=b:
    min=b
elif a>=c and b>=c:
    min=c
else:
    min=a
print("The minimum of three numbers is:",min)           
