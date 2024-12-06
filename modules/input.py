def user_numbers ():
    num1 = float(input("Enter the first number: "))
    while True:
        num2 = float(input("Enter the second number: "))
        if num2 != 0:
            return num1, num2
        else:
            print("Enter a number different than zero")

