def output_result (num1, num2, summ, diff, prod, quot):
    print(f"The sum of {num1} and {num2} is {summ}")
    print(f"The difference between {num1} and {num2} is {diff}")
    print(f"The product of {num1} and {num2} is {prod}")
    print(f"The quotient of {num1} and {num2} is {quot}")

    with open("result.txt", "a") as file:
        file.write(f"The sum of {num1} and {num2} is {summ}\n")
        file.write(f"The difference between {num1} and {num2} is {diff}\n")
        file.write(f"The product of {num1} and {num2} is {prod}\n")
        file.write(f"The quotient of {num1} and {num2} is {quot}\n")
