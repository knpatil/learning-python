# dictionary
d = dict() # map , hash map, hash table

# set value - O(1)
d[5] = "X"   # calculate based on the hash functions - constant time
d["python"] = "programming language" # math function

# get value - O(1)
# value = d[4] # O(1)

# delete value -- O(1)
# del d[7]

# lookup - O(1)
if "python" in d:
    print("I found it.")
else:
    print("not found.")



# pair
# key = 5
# value = X

# set -- key
my_set = {1, 2, 3, 4, 5}  # hash function
# ------------

n = 10
# Give the Big-O performance of the following code fragment:
# 1
for i in range(n): # n - square
   for j in range(n):
      k = 2 + 2

# 2 -- O(n)
for i in range(n):
     k = 2 + 2

# 3 - log n
i = n
while i > 0:
   k = 2 + 2
   i = i // 2

