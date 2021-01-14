lst_1=[12,13,14,15,12,13,14,34,67,56,34,23,12,90,44]
lst_2=[]
for i in lst_1:
    if i not in lst_2:
        lst_2.append(i)
print("The original list was:\n",lst_1)
print("After removing dublicate elements the updated list is:\n",lst_2)            