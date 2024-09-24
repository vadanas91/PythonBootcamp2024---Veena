# subject pts: 
# stroke: odd numbers, rest no stoke.
# '''
# pts = []
# num = [1, 2, 3, 4, 5]
# def add_pts(num):
#     pts.append(num)

# add_pts(num)

# print(f'Adding pts number: {num}')

# strokepts = [1, 3, 5]
# nonstrokepts =[]

# pts = [1,2,3,4,5]
# test = strokepts in pts
# print(f"condition output {test}")

# for num in pts:
#     if num in strokepts:
#         print(f"Patient {num} has stoke")
#     else:
#         nonstrokepts.append(num)
#         print(f"Patient {num} does not have a stoke")

# print(f'Nonstokepts {nonstrokepts}')

# list = [1,2,3,4,5,6,7,10]
# for nums in list:
#     print(f'Individual Numbers: {nums}')

# for index, value in enumerate(list):
#     print(f'list - {index} is {value}')
# '''
# '''
# print multiplication table for 2
# 2 x 1 = 2
# 2 x 2 = 4

# 2 x 10 = 20
# ===
# '''
# ''''''
# const = 2
# numtomult = [1,2,3,4,5,6,7,8,9,10]
# '''


# # pot = 0
# # list = [10, 20, 30]
# # amount = 10

# # for value in list:
# #     print(f' ${str(10 * value)},')

# # listNames = ['Rama','Vina','Ammu','S']

# # amountPerPerson = 10
# # print(type(amountPerPerson))

# # for index,name in enumerate(listNames):
# #     pot = pot + amountPerPerson*index
# #     print(f"After {name} donation, pot is {pot}")

# # print(f'Total number of names in list {len(listNames)}')

# # A = len(listNames)
# # pot = 0
# # pot = pot + A*amountPerPerson
# # print(f"pot is {pot}")


# userinput = input("Type a password: ")
# len_userinput = len(userinput)

# lowerletters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# # uppercaseletters = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

# digits = ['0','1','2','3',4,5,6,7,8,9]

# specialchars = ['!','@','#','$','*','%','&']

# i_1 = 0
# i_2 = 0
# i_3 = 0
# i_4 = 0

# if len_userinput > 8:
#     for thing in userinput:
#         if thing in lowerletters:
#             i_1 = i_1 + 1
#         elif thing in digits:
#             i_2 = i_2 + 1
#         elif thing in specialchars:
#             i_3 = i_3 + 1

# else:
#     print("Your password should be atleast 8 characters length")

# print(f"{i_1},{i_2},{i_3},{i_4}")

# if i_1 >= 1 and i_2>=1 and i_3 >= 1:
#     print("Your password is valid")
# else:
#     print("Your password in not valid. Try again!")

import random
secret_num = str(random.randint(1,99999))
print(secret_num)
user_input = str(int(input("Enter a number from 0 to 9")))
for thing in secret_num:
    print(thing)
    if thing == user_input:
      print ("yes the the number is there")
    else:
      print("the number isnt there")