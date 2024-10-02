# Use a dictionary to store information about a fictional person. 
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

FLfriend = {'first_name': 'Harry', 
            'last_name': 'Potter', 
            'age': '32', 
            'current_city': 'Orlando, FL'}
print(f'My friends name is {FLfriend['first_name']} {FLfriend['last_name']}. He is {FLfriend['age']} years old and resides in {FLfriend['current_city']}.')

# # Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# # Loop through your list of people. As you loop through the list, print everything you know about each person.

FLfriend = {'first_name': 'Harry', 
            'last_name': 'Potter', 
            'age': '32', 
            'current_city': 'Orlando, FL'}
GAfriend = {'first_name': 'Bob', 
            'last_name': 'Builder', 
            'age': '49', 
            'current_city': 'Atlanta, GA'}
UKfriend = {'first_name': 'Hermione', 
            'last_name': 'Granger', 
            'age': '30', 
            'current_city': 'London, UK'}
Friends = [FLfriend, GAfriend, UKfriend]

for person in Friends:
    full_name = person['first_name'] + " " + person['last_name']
    age = int(person['age'])
    current_city = person['current_city']
    
    print(f'{full_name} is {age} years old, lives in {current_city}.')
