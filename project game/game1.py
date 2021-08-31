# snake water and gun game

import random

def gameWin(comp,you):
    if comp==you:
        return None
    
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True

    elif comp=='w':
        if you=='s':
            return True
        if you=='g':
            return False

    elif comp=='g':
        if you=='w':
            return True
        if you=='s':
            return False

print("Welcome to the game of Snake, Water, and Gun🎈🤩 ")

print("Computer's Turn 💻 snake(s), water(w), gun(g)?🤔")
randNo = random.randint(1,3)
print("Computer chose its move")

you = input("your's turn snake(s), water(w), gun(g) ")
if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
elif randNo==3:
    comp = 'g'

print("Your's turn 🧑snake(s), water(w), gun(g)?🤔 ")
a = gameWin(comp,you)

print("Computer choose : " + comp)
print("You choose :" + you)

if a==None:
    print("The game is a tie😐")

elif a:
    print("You Win🤩")

else:
    print("Computer Win🎈")




