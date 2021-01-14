year=int(input("Please enter a year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is Leap year")
        else:
            print(f"{year} is Not Leap year") 
    else:
        print(f"{year} is Leap year")           
else:
    print(f"{year} is Not Leap year")

