# #dictionary
# A = {'color': 'green'}
# print(f'my fav color is {A["color"]}.')
# A['x_position'] = 0

# group = ["Rani", "line"]
# for name in group:
#     print(name)

# for num in range(1,101):
#     print("awesome!")
# # print multiple times, or type number 1-100

# arrival = False
# while arrival == False:
#     response = input("are we there yet?")
#     if response == "yes":
#         print("yay")
#         break
#         # arrival = True

# Modules = random things, already there

# import random

# random_num = random.randint(1,20)
# print(random_num)

# game_over = False
# while game_over == False:
#     guess = int(input("what is the secret number?"))
#     if guess == random_num:
#         print("you win")
#         game_over = True
#     elif guess < random_num:
#         print("guess is too low, try again")
#     elif guess > random_num:
#         print("guess is too high, try again")

import random
# dice_roll = random.randint(1,6)
# print(f'You rolled {dice_roll}.')

def roll():
    roll = random.randint(1,6)
    print(f'You rolled {roll}.')
roll()

def roll(sides):
    roll = random.randint(1,sides)
    print(f'You rolled {roll}.')
roll(10)

roll(100)


# for num in range(1,11):
#     roll()

