#Introductory Dictionaries{}
# email = {
#     "From": "j.smith@example.com", 
#     "To": "zed.shaw@example.com",
#     "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU"
# }

# print(email["From"]) #j.smith@example.com
# print(email["To"]) #zed.shaw@example.com
# print(email["Subject"]) #I HAVE AN AMAZING INVESTMENT FOR YOU

messages = [
    {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
    {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
    {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
    {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'}

]

print(messages[0]["from"])
print(messages[1]["from"])
print(messages[2]["message"])
print(messages[3]["message"])