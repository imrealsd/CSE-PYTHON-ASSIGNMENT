stack=["Engineering","Knowledge","Talent","Experience","Unemployment"]
print("The original stack was:\n",stack)
key=int(input("Enter 0/1 for push/pop:"))
if(key==0):
    value=input("Enter item you want to push:")
    stack.append(value)
    print("After pushing the new stack is:\n",stack)
elif(key==1):
    stack.pop()
    print("After poping the new stack is:\n",stack)        

