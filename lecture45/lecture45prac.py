from random import randint
rand = randint(0,5)
print(rand)

userNum = input("Enter an integer")

try:
    if rand > int(userNum):
        print(rand)
    elif int(userNum) > rand:
        print(int(userNum))
    else:
        print("The number are the same")
except:
    print("Please run the program again and enter an integer")