
# Enter numbers
def enter_numbers():
    entry_number = int(input("Enter the number: "))
    return entry_number

# Simple Calculator
def Mini_Calculator(first_number,i ,second_number):

    if i == "+":
        # Add
        return first_number + second_number
    elif i== "-":
        # Subtract
        return first_number - second_number
    elif i== "*":
        # Multiply
        return first_number * second_number
    elif i== "/":
        # Divide
        if second_number == 0:
            return "Error: Division by zero!"
        return first_number / second_number
    elif i== "%":
        # Modulus
        return first_number % second_number
    elif i== "//":
        # Floor Division
        return first_number // second_number
    else:
        return "Invalid operator"

while True:
    #### Basic calculator with separate entry of numbers and operators
    # first_number = enter_numbers()
    # second_number = enter_numbers()
    # entry_operator = input("Enter the operator (+, -, *, /, %, //): ")
    # result = Mini_Calculator(first_number, entry_operator, second_number)
    # print("result:", result)
    # choice = input("\nDo you want to continue? (y/n): ").lower()
    # if choice != 'y':
    #     break

    #### Calculator using eval function
    input_number_operation = input("Enter your calculation: ")
    result = eval(input_number_operation)
    print("result:", result)
    choice = input("\nDo you want to continue? (y/n): ").lower()
    if choice != 'y':
        break