my_list = list()

my_list.append(0)  # O(1) -- constant time
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print(f"my_list={my_list}")

my_list.insert(2, 10)  # O(n), adding item
print(f"my_list={my_list}")

my_list[3] = 11  # O(1), 3 position, overwrite
print(f"my_list={my_list}")

del my_list[1]  # O(n) -- n is the length of the list
print(f"my_list={my_list}")

# lookup
x = 100
if x in my_list:  # O(n), searching
    print("x is there")
else:
    print("x is not there")

print(my_list[1]) # O(1)
# O(n) -- linear time complexity , changes according n
# nˆ2 -- quadratic 

