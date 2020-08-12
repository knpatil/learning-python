import random

def dice_sum():
    desired_sum = int(input("Desired dice sum:"))
    print("Desired Sum : ", desired_sum)
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice_provided_sum = dice1 + dice2
        print(f"{dice1} and {dice2} = {dice_provided_sum}")
        if desired_sum == dice_provided_sum:
            break

def dice_sum2():
    desired_sum = int(input("Desired dice sum:"))
    print("Desired Sum : ", desired_sum)
    dice_provided_sum = 0
    while desired_sum != dice_provided_sum:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice_provided_sum = dice1 + dice2
        print(f"{dice1} and {dice2} = {dice_provided_sum}")

dice_sum()
dice_sum2()


