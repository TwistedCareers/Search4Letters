"""Search 4 Letters Function"""

"""
letters = {'a', 'e', 'i', 'o', 'u'}
print(letters)

letters = {'a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u'}
print(letters)

letters = set('aeiou')
print(letters)

phrase = set('some random word')
print(phrase)

print(letters.intersection(phrase))
"""


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))


"""
print("_" * 50)
m = search4letters("some random word")
print(m)

m = search4letters("some random word", "power")
print(m)
"""
