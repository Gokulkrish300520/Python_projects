unit = input("Is this temperature is in Celsius or Farenheit (C or F): ")
temp = float(input("Enter the Temperature: "))

if unit=="c" or unit== "C":
    result = (9 * temp)/5 + 32
    print(f"The temperature in Fahrenheit is {round(result)} °F")

elif unit=="F" or unit== "f":
    result = (temp-32) * 5 / 9
    print(f"The temperature in Celsius is {round(result,1)} °C")
else:
    print("Unit is Invalid")
    