import random

people = {"alexis,luis,gerson,itzhak"}
position = random.randint(0,4)
if position == 0:
    print("alexis has to pay the full check")
elif position == 1:
    print("luis has to pay the full check")
elif position == 2:
    print("gerson has to pay the full check")
else:
    print("itzhak has to pay the full check")