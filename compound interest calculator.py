principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter the Principle amount:"))
    if principle<=0:
        print("Principle cant be less than or equal to zero")

while rate<=0:
    rate=float(input("Enter the Interest rate:"))
    if principle<=0:
        print("Interest rate cant be less than or equal to zero")

while time<=0:
    time=int(input("Enter the Time in years:"))
    if time<=0:
        print("Principle cant be less than or equal to zero")

print(principle)
print(rate)
print(time)
total=principle*pow((1+rate/100),time)
print(f"Balance after {time} Year/s : ${total:.2f}")