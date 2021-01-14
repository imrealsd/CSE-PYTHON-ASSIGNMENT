a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
print(f"Before swap a={a} b={b}")
a=a^b 
b=a^b 
a=a^b 
print(f"After swap a={a} b={b}")
