import random
list1 = {}
list1.append("hello")
list1.append(1)
list1.extend([4,5,6,7])
list1.append(random.randint(1,10))
list1.append(int(input("Type a value: ")))

name_string = input("Give the separated names by ',' :")
names = name_string.split(",")
print(names)
print(list1)