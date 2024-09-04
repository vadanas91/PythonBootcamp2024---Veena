# name = input("What is your name?").strip()
# print("hello, " + name + ".")
# print(f"hello, {name}.")



def greet(name = "world"):
    print(f"hello, {name}.")

greet("Veena")
greet("Rama")

# username = input("Enter your username: ")
# greet(username)

def add(a,b):
    print(a+b)

# num1 = int(input("number 1: "))
# num2 = int(input("number 2: "))
# add(num1, num2)

# another way:
num1 = input("number 1: ")
num2 = input("number 2: ")
num1 = int(num1)
num2 = int(num2)
add(num1, num2)