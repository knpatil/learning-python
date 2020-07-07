# reading entire contents in a variable

print("----read file contents in one variable-----")
file_path = 'textfiles/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()

print("Contents of the file is : ", contents.rstrip(), "------")

# read a file line by line
print("----read file one line a time-----")
pi_string = ''
with open(file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()  # strip spaces/line breaks on both sides
print(f"PI = {pi_string}")

print("Type of pi_string is ", type(pi_string))

pi = float(pi_string)
print("Type of pi is ", type(pi))

print("----read file in a list-----")
# create a list of lines from a file
with open(file_path) as file_object:
    lines = file_object.readlines()  # return a list of lines

no_of_lines = len(lines)
print("no of lines =", no_of_lines)

for i in range(no_of_lines):
    print(lines[i].rstrip())

# RAM -- computer
file2 = 'textfiles/pi_million_digits_ssdgsdgs.txt'  # assu
pi_str_2 = ''
with open(file2) as file_object2:
    for line in file_object2:
        pi_str_2 += line.strip()

print("PI:", pi_str_2)
print(f"PI with 52 digits = {pi_str_2[:100]}")
