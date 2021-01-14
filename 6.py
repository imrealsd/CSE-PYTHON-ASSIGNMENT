centre_x=int(input("Enter X coordinate of centre of circle:"))
centre_y=int(input("Enter Y coordinate of centre of circle:"))
R=int(input("Enter radious of circle:"))
x=int(input("Enter X coordinate of checking point:"))
y=int(input("Enter Y coordinate of checking point:"))
check=(x-centre_x)**2 + (y-centre_y)**2 -R**2
if(check<0):
    print(f"point({x},{y}) is inside of the circle")
elif(check==0):
    print(f"point({x},{y}) is on the circle")
else:
    print(f"point({x},{y}) is outside of the circle")    





