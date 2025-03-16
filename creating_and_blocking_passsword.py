saved_password = "Welcome@123"
entered_password = ""
no_of_trys = 0
max_no_of_trys = 8
trys_reached = False

while entered_password != saved_password and trys_reached is not True:
    if no_of_trys < max_no_of_trys:
        a = input("Enter Your Password")
        entered_password += a
        no_of_trys += 1
    else:
        trys_reached = True

if trys_reached is True:
    print("Access Blocked! Try After Sometime")
else:
    print("Access Granted!!!")
