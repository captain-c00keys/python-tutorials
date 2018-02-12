def first():
    print("this is a function")

def intFun(intVal):
    return intVal * 2

def takesTwo(int1, int2):
    return int1 * int2

def funcInside(a, b, c):
    print(takesTwo(intFun(a), b) * c)
    
first()

funcInside(7, 4, 2)