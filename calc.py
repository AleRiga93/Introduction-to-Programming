num1 = float(input("Write a number: "))
while True:
        num2 = float(input("Write the second number: "))
        if num2 != 0:
                quotient = num1 / num2
                break
        else:
            print("Enter a number different than 0")
                

sum = num1 + num2
difference = num1 - num2
product = num1 * num2


print("The sum is : ", sum)
print("The difference is : ", difference)
print("The product is : ", product)
print("The quotient is : ", round(quotient, 2))
