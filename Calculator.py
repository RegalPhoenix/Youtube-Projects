
def main():
    x = input("Hello, what is your name? ").strip().title()
    print(f"Hello {x}, this is your calculator.")

    calc()

def calc():
    while True:
        print("----------------------------------------------------------------------------------------------------------")
        print()
        x = int(input("What's your x? "))
        y = int(input("What's your y? "))

        oper = input("Which operation do you want to do? ").lower().strip()
        match oper:
            case 'multiply' | '*' | 'multiplication':
                print('Answer of your multiplication is', (x*y))
            case 'divide' | 'division' |  '/':
                print('Answer of your division is', (x/y))
            case 'add' | 'addition' | '+':
                print('Answer of your addition is', (x+y))
            case 'subtraction ' | 'minus' | 'subtract' | '-':
                print('Answer of your subtraction is', (x-y))
            case 'power' | "**":
                print("Your answer is,", (x**y))
            case "remainder" | "%":
                print("Your answer is,", (x%y))
            case _:
                print("Please input the correct operation!")
        print()
        ex = input("Would you like to exit the operation? ").lower()
        if ex == 'yes' or ex == 'exit':
            exit()
        print()
        print("----------------------------------------------------------------------------------------------------------")

main()
