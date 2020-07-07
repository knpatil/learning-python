# dictionary is collection of key-value pairs

# students = { "key1":"value1", "key2": "value2", "key3": "value3" }

# color:point

alien = {} # empty dictionary

alien = {"green":100}

alien['red'] = 200
alien['black'] = 90

print(alien)
# access the value
print(alien['black'])

# modify the value
alien['red'] = 500
print(alien)

# remove the value
# del alien['green']
# print(alien)

# name: favorite programming lanauge

print("__" * 40)

# loop through all key/value pairs
for key,value in alien.items():
    print(key, value)
print("__" * 40)

for key in sorted(alien.keys()):
    print(key)
print("__" * 40)

for value in alien.values():
    print(value)
print("__" * 40)
    
