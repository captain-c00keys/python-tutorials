ex1 = input("Guess what my favorite integer is.")

try: #use if error usually occurs when code is ran
    if int(ex1) == 7
        print("That is correct. 7 is my favorite integer.")
    else:
        print("That is not my favorite integer")
except:
    print("Please run the program again and enter an integer")

#ex 2

def divide(top, bottom):
    try:
        print(top/bottom)
    except ZeroDivisionError:
        print("You cannont divide by 0")

divdie("mushroom", True)