# print("""You enter a dark room with two doors.
# Do you go through door #1 or door #2""")

# door = input("Give me just the number (1 or 2): ")
# if door == "1":
#     print("There's a giant bear here eating a cheese cake")
#     print("What do you do?")
#     print("1. Take the cake.")
#     print("2. Scream at the bear")

#     bear = input("Give me just the number (1 or 2): ")

#     if bear == "1":
#         print("The bear eats your face off. \nGood job!")
#     elif bear == "2":
#         print("The bear eats your legs off. \nGood job!")
#     else:
#         print(f"Well, doing {bear} is probably better")
#         print("Bear tuns away")

# elif door == "2":
#     print("You stare into the endless abyss at Cthulhu's retina")
#     print("1. Blueberries")
#     print("2. Yellow jacket clothespins")
#     print("3. Understanding revlovers yelling melodies")

#     insanity = input("Give me just the number (1 - 3): ")

#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello")
#         print("Good job")
#     else:
#         print("The insanity rots your eyes into a pool of muck")
#         print("Good job")
# else:
#     print("You stumble around and fall on a knife and die. \nGood job!")

# from dis import dis
# dis('''
# if door == "1":
#     print("1")
#     bear = input("> ")
#     if bear == "1":
#         print("bear 1")
#     elif bear == "2":
#         print("bear 2")
#     else:
#         print("bear 3")
# ''')


print('''Want to randomly decide which outfit to wear for the day?
Pick a colour:
1. Black
2. Green
3. Yellow
4. Pink
5. Purple
6. Blue
''')
colour = input("Enter a number (1-6): ")
shopping_bag = []

if colour == "1":
    print('''Ooooo, Black my favourite, it goes with everything and brings this balance.
    -------
    Here's the trick, I won't let you choose your outfit but I will decide for you.
    Trust me, you're in safe hands
    If you don't like it you can easily restart the game.
    ''')
#     outfit()


# def outfit():    
    outfit = input("Pick a number from 1-3: ")

    if outfit == "1":
        print(f'''You now have a black dress
        ---
        That would definitely go with a red lipstick and gold jewelerry
        ---
        Should I add this to your shopping bag?
        ''')
        choice = input("Yes or No: ")
        choice = choice.lower()
        print(choice)
        if choice == "yes":
            shopping_bag.append("Black Dress")
        else:
            print(''' Awwwww, You don't like it? Okay sis
            Let's pick another outfit
             ''')
            outfit()
    elif outfit == "2":
        print('''You have a black top
        ---
        Dammmmmuuuunnnn, You are really lucky
        ''')