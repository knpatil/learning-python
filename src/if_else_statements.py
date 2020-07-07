
cars = ['audi','bmw','lexus','ford']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'bmw4' in cars:
    print("I have BMW in list")
else:
    print("no bmw")


# admission fee for a park
# age < 4: free
# 4 - 18: 25
# > 18: 40

age = 3
if age < 4:
    print("admission fee $0")
elif age < 18:
    print("admission fee is $25")
elif age < 65:
    print("$40")
else:
    print("admission fee is $20")

# age < 4 , > 65 -- fee 0
if age < 4 and age > 65:
    print("Free")

x = 5
y = 2
print(x/y)

# -------

def XO(size):
    start = 0
    end = size - 1
    for i in range(0,size):
        for j in range(0, size):
            if j == start or j == end:
                print('x', end='')
            else:
                print('o', end='')
        print()
        start += 1
        end -= 1

print("--------------------")
XO(10)
print("--------------------")





    
