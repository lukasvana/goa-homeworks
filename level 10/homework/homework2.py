#making mathematical calculations with 2 random numbers from 0-9

import random

#number range

numbers = "1""1""2""3""4""5""6""7""8""9"
numbers2 = "1""1""2""3""4""5""6""7""8""9"

#picking random number and labeling it and converting it into int

first_random = int(random.choice(numbers))
second_random = int(random.choice(numbers2))

#printing them

print(first_random , second_random)

#performing mathematical calculations on them and printing

print(first_random + second_random)
print(first_random - second_random)
print(first_random * second_random)
print(first_random / second_random)