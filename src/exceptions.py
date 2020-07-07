
# exceptions: some undesirable errors that occur
# during execution of the program
# if you don't handle the exception(error condition), program will stop there

# try-except block

file_path = 'textfiles/pi_digits_2.txt'
try:
    with open(file_path) as file_object:
        contents = file_object.read()
except FileNotFoundError as error:
    print("Failed to open the file: ", error.filename)

#
# exceptional situation
# exception handling
#
print("I am done reading a file.")
print("I am done reading a file.")
