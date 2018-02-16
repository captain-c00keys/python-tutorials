intList = [1,3,5,7]

def loopList(list_val):
    for items in list_val:
        print(items)

first = range(3)
second = range(2, 5)
third = (2,13,5)

def addingLists(list1, list2, list3):
    new_list = []
    for items in range(0, len(list1)) #could have put any list in the parameter
        new_list.append(list1[items] + list2[items] + list3[items])
    return new_list

def iterList(LOL):
    for items in LOL:
        for num in items:
            print(num)

iterList([[1,2], [0,1], [3,4]])
loopList(intList)

print(addingLists(first, second, third))