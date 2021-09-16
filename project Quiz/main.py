import random

class FlashCard:
    def __init__(self):
        self.fruits = {
            'Apple': 'Red',
            'Orange': 'Orange',
            'Banana': 'Yellow',
            'Guava': 'Green',
            'Lichi': 'Red'
        }

    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            # [(Apple,Red),(Orange,Orange)......]
            print(f"What is color of {fruit}?")
            ans = input()
            if (ans.capitalize()==color):
                print("Correct Answer")
            else:
                print("Wrong Answer")

            option = int(input("Enter 0 if you want to play again\nEnter 1 to exit: "))

            if(option):
                break

print("Welcome to fruit Quiz🤔")
fc = FlashCard()
fc.quiz()

