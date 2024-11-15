num = int(input("Enter a non-negative number: "))

if num <= 0:
    print("Your number is negative")
else:
    result = 1
    i = 1
    while i <= num:
        result *= i
        print(i, ":",  result)
        i += 1
