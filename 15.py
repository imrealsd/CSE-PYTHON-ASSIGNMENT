n=int(input("Enter number of cricketrs:"))
cricketer=[]
print("---Eneter names---:")
for i in range(n):
    name=str(input())
    cricketer.append(name)
value=[]
print("---Enter values:---")
for i in range(n):
    val=int(input())
    value.append(val)
My_dict={}
for i in range(n):
    dict={
        cricketer[i]:value[i]
    }
    My_dict.update(dict)
print("The created dictionary is:\n",My_dict)



