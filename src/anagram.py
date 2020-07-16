#
# given two strings as input: str1, str2
# write a program to check if they are anagram of each other
# e.g
#       str1: heart
#       str2: earth
# return True, if they are anagram
# return False, if not
#

def anagram_1(s1, s2):
    """check if s1 and s2 are anagrams"""
    if len(s1) != len(s2): # short circuit
        return False
    tlist = list(s2) # earth => ['e', 'a', 'r' ...]
    i = 0 # 3
    while i < len(s1): # n times -- for 1 iteration of this while loop
        j = 0
        found = False # 2
        while j < len(tlist) and not found:   # n times
            if s1[i] == tlist[j]:
                found = True
            else:
                j += 1

        if not found:
            return False
        else:
            i += 1
            tlist[j] = None # null value 2 times
    # execution come only all the chars are matching
    return True

# 3 + n * (n + 2 + 2)
#
# O(nˆ2) --> Time complexity, not efficient
#
# anagram solution --> O(n log n) <--
#
# anagram solution --> O(n)  <-- fair, good algorithm
#
# O(1)  <-- constant time , best time complexity
#

print(anagram_1("heart", "earth")) # True
print(anagram_1("python", "earth")) # False
print(anagram_1("python", "typhon")) # True
print(anagram_1("school master", "the classroom")) # True
print(anagram_1("a gentleman", "elegant man")) # True

# What is the time complexity ?
#
# What is the size of the problem? what is n in this case?
# length of string = n
#










