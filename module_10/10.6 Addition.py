try:
    num1_str = input("Enter the first number: ")
    num1 = int(num1_str)

    num2_str = input("Enter the second number: ")
    num2 = int(num2_str)

    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is: {sum}")

except ValueError:
    print("Invalid input. Only numbers are valid. Please try again")