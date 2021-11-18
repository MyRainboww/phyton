
height = int(input("What is your height in cm: "))
can_ride = False

if height > 120:
    can_ride = True

if can_ride:
    age = int(input("How old are you: "))
    ticket = 0
    if age < 12:
        ticket += 5
    elif age <= 18:
        ticket += 7
    elif age <= 45:
        ticket += 9
    photo = input("Want a photo?: (y/n)").lower()
    if photo == "y":
        ticket += 3
    print(f"You have to pay {ticket}")
else:
    print("Te la pelaste cuate")

