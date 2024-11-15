def temp_to_fah (celsius):
    result = (celsius * 9) / 5 + 32
    return result
def temp_to_cel (fah):
    result = (fah - 32) * 5 / 9
    return result

choice = input("Do you want to convert your yemperature in Fahrenheit or Celsius? Type F or C ").lower()
if choice == "f":
    celsius = float(input("Write the temperature in Celsius: "))
    print("The temperature in Fahrenheit is: ", round(temp_to_fah (celsius), 2), "*F")
elif choice == "c":
    fah = float(input("Write the temperature in Fahrenheint is: "))
    print("The temperature in Celsius is: ", round(temp_to_cel (fah), 2), "*C")
else:
    print("Incorrect answer!!! Type F or C")
                        






