#Introductory Dictionaries{}
email = {
    "From": "j.smith@example.com", 
    "To": "zed.shaw@example.com",
    "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU"
}

# print(email["From"]) #j.smith@example.com
# print(email["To"]) #zed.shaw@example.com
# print(email["Subject"]) #I HAVE AN AMAZING INVESTMENT FOR YOU

messages = [
    {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
    {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
    {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
    {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'}

]

# print(messages[0]["from"])
# print(messages[1]["from"])
# print(messages[2]["message"])
# print(messages[3]["message"])


fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
];

# print(fruit[0]['count'])
# print(fruit[0]['rating'])
# print(fruit[2]['count'])
# print(fruit[1]['kind'])
# print(fruit[3]['kind'])
# print(fruit[3]['count'])
# print(fruit[0]['kind'])

cars = [
    {'type': 'Cadillac', 'color': 'Black', 'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red', 'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue', 'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White', 'size': 'Baby', 'miles': 7890}
];

# print(cars[0]['size'])
# print(cars[1]['color'])
# print(cars[2]['miles'])
# print(cars[3]['color'])
# print(cars[3]['miles'])
# print(cars[0]['color'])
# print(cars[0]['miles'])
# print(cars[2]['color'])

languages = [
    {'name': 'Python', 'speed': 'Slow', 'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate', 'opinion': ['Alright', 'Bizzare']},
    {'name': 'Per16', 'speed': 'Moderate', 'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast', 'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast', 'opinion': ['Fun', 'Difficult']}
];

print(languages[0]['speed'])
print(languages[1]['opinion'][0])
print(languages[3]['opinion'][1])
print(languages[3]['speed'])
print(languages[4]['opinion'][1])
print(languages[2]['opinion'][0])
print(languages[3]['opinion'][0])
print(languages[2]['opinion'][1])
print(languages[1]['speed'])
