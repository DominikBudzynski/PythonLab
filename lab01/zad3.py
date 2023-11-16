import os

path = 'C:/Users/domin/Desktop/Nowy folder/zad3/tekst.txt'

def removeWords(path, word):
    fd = open(path, 'r')
    fContent = fd.read()
    if (word in fContent):        
        newContent = fContent.replace(word, '')        
        open(path, 'w').write(newContent)

removeWords(path, 'dwa')