my_dict={
    "Sumit": 52,
    "Subha": 62,
    "Debjyoti":70,
    "Ankur": 55,
    "Atanu": 57
}
print("Before sorting the dictionary was:\n",my_dict)
ascending_values=sorted(my_dict.values())
ascending_dict={}
for i in ascending_values:
    for k in my_dict.keys():
        if my_dict[k]==i:
            ascending_dict[k]=my_dict[k]
print("\t")
print("After sorting in ascending order:\n",ascending_dict)
descending_values=reversed(ascending_dict.values())
descending_dict={}
for i in descending_values:
    for k in my_dict.keys():
        if my_dict[k]==i:
            descending_dict[k]=my_dict[k]
print("\n")
print("After sorting in descending order:\n",descending_dict)



 



