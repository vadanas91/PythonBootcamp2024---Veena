name = input("Hello, What is your name?: ").capitalize()

age = int(input("What is your age?: "))

def age_100(age):
    return((age+100))

def greet(name):
    print(f"Hello, {name}! Hope you are having a great day! You will be {str(age_100(age))} in 100 years.")
greet(name)

# Create a tip calculator program using functions and user input. Use a return statement in your function.

X = abs(float(input("Here is a tip calculator. What is your total bill without tip?: " )))
Y = abs(float(input("What percentage do you want to tip?: " )))

def Total(X,Y):
  return((Y/100)*(X))

print(f"You will be tipping ${round(Total(X,Y),2)} for ${round(X,2)}. Your total bill with tip will be ${round(Total(X,Y) + X,2)}.")