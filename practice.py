## List
# cities = ['Los Angeles', 'London', 'Tokyo']
# print(cities[0])
# print(len(cities))
# cities[0] = 'Jeju'
# print(cities)
# cities += ['Washington']
# print(cities)

# developer = ['Jessy', '25', 'Front-End']
# developer.append(6)
# print(developer)
# print(type(developer[1]))

# languages = ['English', 'Yoruba', 'Igbo', 'Hausa', 'Tiv']

# for index, language in enumerate(languages, 1):
#     print(f'{index}. {language}')

# ids =[1, 2, 3, 4, 5]
# print(list(zip(ids, languages)))

# for language, lang_id in zip(languages, ids):
#     print(f'Language: {language}')
#     print(f'ID: {lang_id}')

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

# long_words = list(filter(is_long_word, words))
# print(long_words) # ['mountain', 'river', 'cloud']



