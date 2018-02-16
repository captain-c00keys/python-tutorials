#two different ways to iterate through a string using range() and a for loop
#ex 1
ex_str = "example"

for char in ex_str: #char is a placeholder
    print(char)

#ex 2
ex_str = "example"

for char in range(len(ex_str)):
    print(ex_str[char])

# using "," in print statement in for loop
#ex 3
ex_str = "example"

for char in ex_str:
    print(char, end=" ")

#ex 4
ex_str = "example"

for char in ex_str:
    print(char, end="Z") #puts Z after every letter in example

#ex 5
ex_dict = {"first": 1, "second": 2, "third": 3} #

for key in ex_dict:
    print(key + " " + str(ex_dict[key]))

#zip()
#ex 6
list1 = [4,0,11,3]
list2 = [1,1,9,18]

for items1, items2 in zip(list1, list2)
    if items1 > items2:
        print(items1)
    elif items1 < items 2:
        print(items2)

#for/else
#ex 7
exTup = (3,5,7)

for item in exTup:
    print(item)
else:
    print(9)

#ex 8
exTup = (3,5,7)

for item in exTup:
    if item < 7:
        print(item)
    else:
        break
else:
    print(9)