import time

start_time = time.time()

filename = 'textfiles/programming.txt'

print(f"Creating {filename} ...")

# with open(filename, 'w') as file_object:
#     file_object.write("I like python programming.\n")
#     file_object.write("It is very flexible and ")
#     file_object.write("fun.")

with open(filename, 'a') as file_object:
    file_object.write("\nI learned about reading files.\n")
    file_object.write("and writing to files in  ")
    file_object.write("python.")

print(f"added more lines to {filename}.")

end_time = time.time()
total_time = end_time - start_time
print("This program took {:.5f}s to run.".format(total_time))