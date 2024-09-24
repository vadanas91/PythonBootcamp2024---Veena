# 1. Create a program that removes all the vowels from user input and produces the outcome back to the user.

userinput1 = input('Enter in a phase and I will remove the vowels:')
vowels =['a', 'e', 'i', 'o', 'u']
output = " "
for char in userinput1:
    if char in vowels:
        char = " "
        output = output + char
    else:
        output = output + char
print(output)

# 2. Create a password validator program that only accepts a password that fits a set of requirements.
#     These requirements are up to you. Make sure the user knows the requirements before they try a password.
#     Do not allow the program to end until the password meets all your requirements.
#     Try to use a dictionary to solve this, if you can manage it.

import string
specialchars = ['!','@','#','$','*','%','&','^']
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
nums = string.digits
def password(userinput2):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0

    if len(userinput2)<8:
        print("Password needs to have atleast 8 characters.")

    else:
        for thing in userinput2:
            if thing in lowercase:
                counter1 = counter1 + 1      
            elif thing in uppercase:
                counter2 = counter2 + 1  
            elif thing in specialchars:
                counter3 = counter3 + 1  
            elif thing in nums:
                counter4 = counter4 + 1  

    if counter1>=1 and counter2>=1 and counter3>=1 and counter4>=1:
        return(1)   
    else:
        return(2)       
    # print (f"{counter1}, {counter2}, {counter3}, {counter4}")

while_check = 0
while while_check == 0:
    userinput2 = input('Enter a password with minimum 8 characters, 1 lowercase, 1 uppercase, 1 number, and 1 special (!@#$%^&*):')
    X = password(userinput2)
    if X == 1:
        while_check = 1
        print("Your password is valid and saved for future logins!")
    elif X == 2:
        print("Your password is invalid and try again! Password must have minimum 8 character, 1 lowercase, 1 uppercase, 1 number, and 1 special character (!@#$%^&*)")
        while_check = 0