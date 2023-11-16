import os

folder = "C:\\Users\\domin\\Desktop\\Nowy folder"

def printTree(path, num = 0):
    dirs = os.listdir(path)   
    for dir in dirs:              
        actualDir = path + "\\" + dir           
        if (os.path.isdir(actualDir)):            
            print('\t' * num + actualDir)
            printTree(actualDir, num + 2)
        else:            
            print('\t' * num + actualDir)

printTree(folder)