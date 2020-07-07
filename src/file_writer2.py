

with open("my_file.txt", 'w') as file_object:  # opens only
    while True:
        name = input("What is your name : ")
        if name == 'quit':
            break
        file_object.write(name)

print("Done.")
