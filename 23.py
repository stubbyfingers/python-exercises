# Lists
# fruit = [[1, 2, 3], ["apples", "oranges", "grapes"], ["Benz", "Tesla", "Toyota"]]
# print(fruit)

# inventory = [["Buick", 10], ["Corvette", 1], ["Toyota", 4]]
# buicks = inventory[0]
# buick_count = buicks[1]
# print(buicks)
# print(buick_count)
# count_of_toyota = inventory[2][1]
# print(count_of_toyota)

fruit = [["Apples", 12, "AAA"], ["Oranges", 1, "B"], ["Pears", 2, "A"], ["Grapes", 14, "UR"]]
cars = [["Cadillac", ["Black", "Big", 34500]], ["Corvette", ["Red", "Little", 1000000]], ["Ford", ["Blue", "Medium", 1234]], ["BMW", ["White", "Baby", 7890]]]
languages = [["Python", ["Slow", ["Terrible", "Mush"]]], ["Javascript", ["Moderate", ["Alright", "Bizarre"]]], ["Per16", ["Moderate", ["Fun", "Weird"]]], ["C", ["Fast", ["Annoying", "Dangerous"]]], ["Forth", ["Fast", ["Fun", "Difficult"]]]]

fruit1 = fruit[0][1]
fruit2 = fruit[0][2]
fruit3 = fruit[2][1]
fruit4 = fruit[1][0]
fruit5 = fruit[3][0]
fruit6 = fruit[3][1]
fruit7 = fruit[0][0]

cars1 = cars[0][1][1]
cars2 = cars[1][1][0]
cars3 = cars[2][1][2]
cars4 = cars[3][1][0]
cars5 = cars[3][1][2]
cars6 = cars[0][1][0]
cars7 = cars[0][1][2]
cars8 = cars[2][1][0]

lang1 = languages[0][1][0]
lang2 = languages[1][1][1][0]
lang3 = languages[3][1][1][1]
lang4 = languages[3][1][0]
lang5 = languages[4][1][1][1]
lang6 = languages[4][1][1][0]
lang7 = languages[3][1][1][0]
lang8 = languages[2][1][1][1]
lang9 = languages[1][1][0]


print(fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7)
print(cars1, cars2, cars3, cars4, cars5, cars6, cars7, cars8)
print(lang1, lang2, lang3, lang4, lang5, lang6, lang7, lang8, lang9)

print(cars[1][1][1]) # "Little"
print(cars[1][1][0]) # "Red"
print(cars[1][0]) # "Corvette"
print(cars[3][1][1]) # "Baby"
print(fruit[3][2]) # "UR"
print(languages[0][1][1][1]) # "Mush"
print(fruit[2][1]) # "2"
print(languages[3][1][0]) # "Fast"``