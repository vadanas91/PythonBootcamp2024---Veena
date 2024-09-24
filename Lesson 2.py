# #todo prompt for hours worked
# #int - whole number, float = decimals
# Hours_worked= float(input("How many hours have you worked?:"))
# Hourly_rate= float(input("Your hourly rate?:"))
# gross_pay = Hours_worked * Hourly_rate
# #present answer
# print(gross_pay)


#create function
# def gross_pay_calc(hours_worked, hourly_rate):
#     print (hours_worked * hourly_rate)
# gross_pay_calc(40,15)

# different way
# def gross_pay_2():
#     Hours_worked= float(input("How many hours have you worked?:"))
#     Hourly_rate= float(input("Your hourly rate?:"))
#     print(Hours_worked * Hourly_rate)
#gross_pay_2()

'''
#conditional lesson
age = int(input("what is your age?"))
if age >100:
    print("Get an eye exam!")
elif age >= 16:
    print("You are eligible for a drivers license")
elif age <0:
    print("Not a valid age")
else:
    print("You are not old enough for a driver's license")

print("Code Complete")
'''
'''
stop_light = "green"
if stop_light == "green":
    print("Go!")
elif stop_light == "red":
    print("Stop!")
else: 
    print("Not a valid color")
'''
'''
#boullean - switches, changes true/false

is_raining = True
if is_raining == False:
    print("Get an umbrella")
else:
    print("No umbrella needed")
is_raining = True
print (is_raining)
'''
'''
#stringing
backpack = ["phone", "keys", "book"]
print (backpack)
print ("your dropped your phone, OH NO!")
backpack.remove("phone")
if "phone" in backpack:
    print("yay, leave the house")
else:
    print("forgot your phone")

print("you found gold")
backpack.append ("gold")

print(backpack)
'''
'''
#In class assignment:
Hours_worked= float(input("How many hours have you worked?:"))
Hourly_rate= float(input("Your hourly rate?:"))


# def overtime (Hours_worked, Hourly_rate):
#     Hours_worked= float(input("How many hours have you worked?:"))
#     Hourly_rate= float(input("Your hourly rate?:"))
# print(gross_pay)

# Hours_worked = 50
# Hourly_rate = 20

if Hours_worked >= 40:
    extra_hours = Hours_worked - 40
    print ((extra_hours) * (Hourly_rate *1.5) + (40 * Hourly_rate))
else:
    gross_pay = Hours_worked * Hourly_rate
print(gross_pay)

# BOOK: python for everybody, python crash course 


# number from user:
# divide by 3 or say not or invalid entry. 

'''