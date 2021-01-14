upper=500
lower=1
for num in range(lower,upper+1):
    sum = 0
    order=len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit **order
        temp=temp//10
    if num == sum:
        print(num," ",end="")

       






        