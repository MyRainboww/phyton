import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1 = [rock,paper,scissors]

choice = int(input("Make a choice 0-rock 1-paper 2-scissors: "))
computer = random.randint(0,2)

if choice == 0 and computer == 2:
    print("You win")
elif choice == 2 and computer == 0:
    print("You lose")
elif choice > computer:
    print("User wins")
elif choice < computer:
    print("Computer wins")
elif choice == computer:
    print("It's a tie")

print("User")
print(list1[choice])
print("Compute")
print(list1[computer])