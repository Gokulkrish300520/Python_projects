weight = float(input("Enter your weight: "))
unit = input("Kilo-gram or Pounds? (K or L): ")
if unit=="K":
    result=weight * 2.205
    unit="Lbs"
    print(f"{result} {unit}")
elif unit=="L":
    result=weight /  2.205
    unit="Kgs"
    print(f"{round(result)} {unit}")
elif unit==" ":
    print(f"The {unit} is not valid")