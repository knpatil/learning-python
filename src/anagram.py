#
# given two strings as input: str1, str2
# write a program to check if they are anagram of each other
# e.g                   0 1 2 3 4
#       str1: heart  -> a e h r t (sort alphabetically)
#       str2: parth  -> a h p r t (sort
#
# return True, if they are anagram
# return False, if not
#
import time

# 3 different solutions
#
# 1  <- log n <- n <- n log n <- nˆ2 <- nˆ3 <- exponential time
#

def anagram_3(s1, s2):
    start_time = time.time()
    print(f"s1={s1}")
    print(f"s2={s2}")

    # n
    if len(s1) != len(s2): # short circuit
        print("different lengths")
        return False

    # 26
    c1 = [0] * 26 # create a list of 26 integers
    # 26 --> constant <- something that doesn't change for different inputs
    c2 = [0] * 26

    print(f"c1={c1}")
    print(f"c2={c2}")

    # count the characters in first string
    # n
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')  # find the slot where to store count
        c1[pos] = c1[pos] + 1     # increment count

    print(f"c1={c1}")

    # n
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')  # find the slot where to store count
        c2[pos] = c2[pos] + 1     # increment count

    print(f"c2={c2}")

    # n
    for i in range(0, len(c1)):
        if c1[i] != c2[i]:
            return False

    end_time = time.time()
    return True, "{:.2}".format(end_time - start_time)

# n + n + n + n = 4n => n
# 25
# 625, 34.94, 25
# 1500
# 2250000, 4764.13, 1500

def anagram_2(s1, s2):
    start_time = time.time()
    print(f"s1={s1}")
    print(f"s2={s2}")

    if len(s1) != len(s2):  # short circuit
        print("String lengths are different... exiting.")
        return False

    l1 = list(s1)   # convert string s1 -> list of characters
    l2 = list(s2)

    print(f"l1={l1}")
    print(f"l2={l2}")

    l1.sort()   # internally, it uses sorting algorithms, n * log n , nˆ2
    l2.sort()   # n log n

    print(f"l1={l1}")
    print(f"l2={l2}")

    # n times
    for i in range(0, len(s1)):
        if l1[i] != l2[i]:
            return False

    end_time = time.time()

    return True, "{:.2}".format(end_time - start_time)   # all characters matching

# n log n + n log n =  n log n + n # dominant term ? = n * log n

def anagram_1(s1, s2):
    """check if s1 and s2 are anagrams"""
    start_time = time.time()

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

    end_time = time.time()

    return True, "{:.2}".format(end_time - start_time)

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

# print(anagram_3("heart", "earth")) # True
# print(anagram_3("python", "earth")) # False
# print(anagram_3("python", "typhon")) # True

print(anagram_1("agentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentleman", "agentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentleman")) # True, scope of the problem
print(anagram_2("agentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentleman", "agentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentleman")) # True, scope of the problem
print(anagram_3("agentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentleman", "agentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentlemanagentleman")) # True, scope of the problem


# What is the time complexity ?
#
# What is the size of the problem? what is n in this case?
# length of string = n
#

