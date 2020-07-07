vowels = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u']

set_of_vowels = {'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'}
my_dict = {"k": "v", "k2": "v2"}

print("list: ", vowels)
print("set: ", set_of_vowels)

# properties : it holds only unique
print("length: ", len(set_of_vowels))

set_of_vowels.add('o')
print("set: ", set_of_vowels)

# set is very efficient / fast / optimized

vowels2 = 'aeiouuuuuuuaaaaaaiiiiiiii'
set_of_vowels2 = set(vowels)  # create a set with all the characters
print(set_of_vowels)

persons = ["Erik", "David", "Lisa", "Lisa", "David"]
set_of_persons = set(persons)
print("set of persons: ", set_of_persons)

# set methods
set1 = set("aeiou")
set2 = set("hello")
print("set 1: ", set1)
print("set 2: ", set2)

print("Union:", set1.union(set2))  # union of sets
print("Intersection: ", set1.intersection(set2))  # intersection
print("Difference: ", set1.difference(set2))  # print values which are in set1 but not in set2

# set lookup is very fast
