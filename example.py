import timeit
from wordfinds import WordFind, WordBank


words = [
    'icecream',
    'house',
    'ice',
    'fire'
]

test = WordFind(
    (10,10),
    WordBank(words)
)


print(test)
print('Found words in', timeit.Timer(test.find_words).timeit(1))
finds = test.find_words(3)
print("Are the original words found?", min([x.upper() in finds for x in words]))

