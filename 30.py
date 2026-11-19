people = int(input("Give me the number of people: ")) #20
cats = int(input("Give me the number of cats: ")) #30
dogs = int(input("Give me the number of dogs: ")) #15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs")


# from dis import dis

# dis('''
# if people < cats:
#     print("Too many cats! The world is doomed!")
# ''')