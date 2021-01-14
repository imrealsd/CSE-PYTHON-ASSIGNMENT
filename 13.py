print("Enter Starting Date")
a,b,c=int(input("DD:")),int(input("MM:")),int(input("YY:"))
print("Enter Ending Date")
d,e,f=int(input("DD:")),int(input("MM:")),int(input("YY:"))
start=(a,b,c) 
end=(d,e,f)
dt1=start[2]*365+start[1]*30+start[0]
dt2=end[2]*365+end[1]*30+end[0]
total=dt2-dt1
print("Total number of days between two dates are:",total,("(Approx.)"))
