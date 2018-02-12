emptyDic = {}

emptyDic["just"] = 3
emptyDic["do"] = 4
emptyDic["it"] = 5

print(emptyDic)
print(len(emptyDic))
print(emptyDic["just"])

emptyDic["just"] = 8
print(emptyDic("just"))

del emptyDic["do"]
print(emptyDic)