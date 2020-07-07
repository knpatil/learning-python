
# every python file is treated as a module

def addition(num1, num2):

    return num1 + num2


def main():
    # run this code only if you are running this as a main program
    print(f"NAME OF THE PROGRAM = {__name__}")
    print("this is a math module")
    print(addition(4, 8))

if __name__ == '__main__':
    main()



