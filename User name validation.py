name = input("Enter your name: ")
if len(name)>12:
    print("Enter name less than 12 characters")
elif " " in name:
    print("Your name has whitespace.Enter name without space")
elif not name.isalpha():
    print("The entered name contains invalid Characters . It must contain only alphabets")
else:
    print("Name Accepted")