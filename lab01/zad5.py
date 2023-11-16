import re

firstPath = "C:/Users/domin/Desktop/Nowy folder/zad5/tekst1.txt"
secondPath = "C:/Users/domin/Desktop/Nowy folder/zad5/tekst2.txt"

dict = {"jeden" : "1",
        "dwa" : "2",
        "trzy" : "3",
        "cztery" : "4",
        "piec" : "5"}

list = ["jeden", "dwa", "trzy", "cztery", "piec"]

def removeWords(path, word):
    fd = open(path, 'r')
    fContent = fd.read()
    fContent = re.sub(word, "", fContent) 
    open(path, 'w').write(fContent)

def replaceWDict(path, wordsList, changeDict):
    fd = open(path, 'r')
    fContent = fd.read()
    for word in wordsList:
        fContent = re.sub(word, changeDict[word], fContent)    
        open(path, 'w').write(fContent)


removeWords(firstPath, 'dwa')

replaceWDict(secondPath, list, dict)