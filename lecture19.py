name = input("Enter your name")

nameLen = len(name)

if len(name) < 4:
    print("Your name is less than 4 characters")

elif len(name) < 10:
    print("Your name is at least 4 characters and less than 10")

else:
    print("Your name is too long")