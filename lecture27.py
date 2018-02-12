newList = [1, 2, 3, 4, 4, 6]
print(newList)

newList[4] = 5 #for reassigning number in list (5) by index (4)
print(newList)

newList.append(7) #puts 7 at end of list
print(newList)

print(newList[:4])
print(newList[2:5])
print(newList[5:])

print(newList.index(7))
print(newList.insert(0, 0)) #using insert is to insert 0 at 0 index
print(newList.remove(3))
print(newList.pop())