from art import logo

print(logo)

def arthemetic(operation, number_1, number_2):
    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    elif operation == '/':
        return number_1 / number_2
    elif operation == '*':
        return number_1 * number_2
    elif operation == '%':
        return number_1 % number_2
    else:
        print("Enter a valid operation")

def calculator():
    number_1 = float(input("Enter first number: "))
    while True:
        operation = input("Enter operator \n '+'\n '-'\n '*'\n '/'\n '%'\n: ")
        number_2 = float(input("What's next number "))
        result = arthemetic(operation, number_1, number_2)
        print(f"Result: {result}")
        yn = input(f"Do you want to continue with {result} (y/n): ").lower()
        if yn == 'y':
            number_1 = result
            continue
        elif yn == 'n':
            calculator()
            
calculator()
