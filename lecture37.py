from random import randint
counter = 5

while counter < 10:
    print(counter)
    if counter == 7:
        print("counter is equal to 7")
        break
    counter = randint(5,10)
else: 
    print("counter is equal to 10")