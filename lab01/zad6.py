import random

selectList = random.sample(range(1, 1000), 50)
insertList = selectList.copy()
controlList = selectList.copy()

print("Before sorting: ")
print(selectList)

def selectSort(list):
    for i in range(0, len(list)):
        minimum = min(list[i:])
        index = list.index(minimum)
        list[index] = list[i]
        list[i] = minimum        

def insertSort(list):
    size = len(list)
    for i in range(1, size + 1):        
        value = list[size - i]
        for j in range(i, 0, -1):                        
            if (list[size - j] < value):
                list[size - j - 1] = list[size - j]
                list[size - j] = value            

print("Select Sort")
selectSort(selectList)
print(selectList)    

print("Insert Sort")
insertSort(insertList)
print(insertList)

print("Checking:")
controlList.sort()
print(controlList)

if (selectList == controlList):
    print("\nSelect Sort works fine.")
else:
    print("\nSelect Sort does not work.")

if (insertList == controlList):
    print("\nInsert Sort works fine.")
else:
    print("\nInsert Sort does not work.")
