
vowels = ['a', 'e', 'i', 'o', 'u']

# write a python program to count vowels in a given word


def frequency_count(word):
    found = {}

    for letter in word:
        if letter in vowels:
            found.setdefault(letter, 0)
            found[letter] += 1

    print(found)


text = "hitchhiker"
frequency_count(text)

#
# Set
#

