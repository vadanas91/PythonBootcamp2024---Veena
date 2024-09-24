import random
secret_num = random.randint(1, 99999)
print(secret_num)
user_input = input("Enter a number from 0 to 9")
# for thing :
#     if thing == secret_num:
#       print ("yes the the number is there")
#     else:
#       print("the number isnt there")
            
# '''
#in class assignment:
# For loop in string
birthday = input("What is your bday?")
for letter in birthday:
    if letter == "J":
        print("Your bday month has J in it")
    else:
        print('Your bday does not have a J')
'''
'''
#while loop
counter = 0
while counter < 10:
    print('I am awesome!')
    counter = counter + 1
    print(counter)
'''
guess_counter = 0
## determine secret number
secret_num = random.randint(1, 10)
## user input, ask for guess
## user_guess = input("Guess the secret number?")
## assign user input to variable
## check if variable matches secret number if not ask the user again
## keep track of number of guesses
## stop playing game when user guesses correcting or if 10 guesses
'''
while guess_counter < 10:
    guess_counter = guess_counter + 1
    user_guess = int(input("What is the secret number?"))
    if user_guess == secret_num:
        print(f"You win! It took you {guess_counter} tries.")
        break
    # else:
    #     if user_guess < secret_num:
    #         print("Try a higher number, guess again")
    #     elif user_guess > secret_num:
    #         print("Try lower, guess again")

    elif user_guess < secret_num:
            print("Try a higher number, guess again")
    else:
            print("Try lower, guess again")

'''
'''
backpack = ["book", 'radio', 'phone', 'water']
print(backpack[0])
print(backpack[0:2])
print(backpack[:2])
#prints last elements
print(backpack[-1])

phrase = "I am awesome... but only on tues"
print(phrase[5:])
print(phrase[:15])
'''
# ## ask user name
# password = "letmein"
# counter = 0 
# while password < 3:
#     counter = counter + 1
#     password = input("Enter your password")
#     if password:
#         password == "letmein"
#         print("you in")
#     else:
#       password != "letmein"
#       print("You tried 3 times. You are locked.")