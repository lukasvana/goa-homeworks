#made a guessing machine 

import random

list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
num = random.choice(list)

player_choice = int(input("select a number through 1-10:"))


if player_choice == num:
    print("I guessed " + str(num) +" you won")
else:
    print("I guessed " + str(num) +" you lost")