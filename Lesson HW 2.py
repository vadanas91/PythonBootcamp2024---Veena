'''
1. Create an empty list called “friends”. Create a function that adds a friend to the friends list and
    a function that removes a friend from the friends list. Both of the functions should take one parameter
    which is the name of the person that will be added or removed.
2. Use the functions you created in step 1 to add 5 people to your friends list using your function.
    Then remove two friends from your list using your remove function. If the friend is not in the list,
    print a message that says the friend is not in the list and can’t be removed. Finally, print out your final 
    friend list.
#stringing
'''
Friends = []

def add_friends(name):
   Friends.append(name)

add_friends("Zina")

print(f"List after addition: {Friends}")

def remove_friends(name):
    if name in Friends:
        Friends.remove(name)
    else:
        print(f"{name} is not on the list. Cannot remove within function")

remove_friends("Zina")

print(f"List after removing {Friends}")

add_friends("Lina")
add_friends("Vina")
add_friends("Mina")
add_friends("Nina")
add_friends("Tina")

# friends2add = ['Lina', 'Vina', 'Mina', 'Nina', 'Tina']
# Friends.extend(friends2add)

print(f"List after adding 5 names: {Friends}")

# friends2remove = ['Mina', 'Tina','Rama']
# remove_friends(friends2remove)

remove_friends("Mina")
remove_friends("Tina")
remove_friends("Rama")

print(f"List after removing 2 names: {Friends}")

# # print(f'removing within loop')

# for name in friends2remove:
#     remove_friends(name)
# print(f"List after removing 3 items: {Friends}")

# for name in friends2remove:
#     if name in Friends:
#         Friends.remove(name)
#     else:
#         print(f"{name} is not on the list. Cannot remove.")

# print(f"Total friends after removing {Friends}")