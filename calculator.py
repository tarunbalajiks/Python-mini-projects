# ===== load_thecode =====#
# defining math operations
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

# ===== load_thecode =====#
# maincode
print('''Please select operation \n 1. Add  
2. Subtract 
3. Multiply
4. Divide 
5. Quit''')
while True:
    select = input("Select operations form 1, 2, 3, 4, Quit(5):")

    if select == '5':
        break
    else:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print(number1, number2)
        if select == '1':
            print(add(number1, number2))
        elif select == '2':
            print(subtract(number1, number2))
        elif select == '3':
            print(multiply(number1, number2))
        elif select == '4':
            print(divide(number1, number2))
        else:
            print("Invalid input")
