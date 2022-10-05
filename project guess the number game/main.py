#Guess the Number Game
import random
for i in range(0,3):
    number = random.randint(1,10)
    user = int(input("Guess the number  "))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
    if user != number:
        print(f"Your guess is incorrect the number is {number}")