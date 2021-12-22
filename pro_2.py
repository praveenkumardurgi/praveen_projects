color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]

list1 = []

#print(set(color1) & set(color2))

for i in color1:
    if i in color2:
        list1.append(i)

print(list1)
