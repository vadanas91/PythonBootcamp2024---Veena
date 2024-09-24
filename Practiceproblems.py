#BMI calculator
# bmi_calculator which takes user inputs height and weight
# bmi category - user is underweight, normal weight, overweight or obese.

# weightlbs = float(input("Lets do a BMI calc. What is your weight in lbs?:" ))
# heightinc = float(input("Next, what is your height in inches?:" ))

# BMIcalc = ((weightlbs)/(heightinc * heightinc)) * 703

# if BMIcalc <18.5:
#     print("You are underweight. EAT!")
# elif BMIcalc >=18.5 and BMIcalc<24.9:
#     print("You are normal weight")
# elif BMIcalc >=24.9 and BMIcalc<29.9:
#     print("You are overweight")
# else:
#     print("You are obese and going to DIE!")

userinput=input("Enter a word: ")
def Palindrome(userinput): 
    if(userinput==userinput[::-1]):
        return("Yes, the word is a palindrome!") 
    else: 
        return("No, the word is not a palindrome.") 
print(Palindrome(userinput))