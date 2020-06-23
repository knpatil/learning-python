
names = []
while True:
    username = input("Enter name:")
    if username is None or username == "":
        break
    names.append(username)

print("List of names: ", names)

count_table = {}
for name in names:
    if name in count_table:
        cnt = count_table[name]
        cnt += 1
        count_table[name] = cnt
        print("cnt=",cnt) # debugging
    else:
        count_table[name] = 1

for name in sorted(count_table.keys()):
    # print("Entry [{0}] has count {1}".format(name, count_table[name]))
    print("Entry [%s] has count %d" % (name, count_table[name]))


