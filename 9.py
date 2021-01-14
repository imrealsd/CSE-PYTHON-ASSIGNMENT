import math
for a in range (1,31):
    for b in range (1,31):
        c= math.sqrt(a*a+b*b)
        if (c<31):
            if(c%1==0):
                print(f"{a,b,int(c)}",",",end="")


           


      