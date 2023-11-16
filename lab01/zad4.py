import os

path = "C:/Users/domin/Desktop/Nowy folder/zad4/tekst.txt"

dict = {"jeden" : "1",
        "dwa" : "2",
        "trzy" : "3",
        "cztery" : "4",
        "piec" : "5"}

list = ["jeden", "dwa", "trzy", "cztery", "piec"]

def replaceWDict(path, wordsList, changeDict):
    fd = open(path, 'r')
    fContent = fd.read()
    for word in wordsList:        
        if word in changeDict and word in fContent:
            fContent = fContent.replace(word, changeDict[word])
        open(path, 'w').write(fContent)


# replaceWDict(path, ["jeden"], dict)
replaceWDict(path, list, dict)