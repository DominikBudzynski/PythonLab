import multiprocessing
import random
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def selectSort(list):
    for i in range(0, len(list)):
        minimum = min(list[i:])
        index = list.index(minimum)
        list[index] = list[i]
        list[i] = minimum
    return list

def parallelSorting(data, processCount = 1):
    parts = []
    maxPartSize = len(data) // processCount
    
    for i in range(0, len(data), maxPartSize):
        parts.append(data[i: i + maxPartSize])    

    with multiprocessing.Pool(processCount) as pool:
        sorted_parts = pool.map(selectSort, parts)
        
    return sorted_parts[0]

if __name__ == "__main__":
    dataCount = 1000
    dataStep = 150

    dataTabs = []   
    howMuchData = [] 
    timeTabs = [[], [], [], [], []]

    sortedData = []    

    for i in range(1, 6):
        dataTabs.append(random.sample(range(1, dataCount), dataStep * i))        
        start = time.time()                        
        sortedData.append(parallelSorting(dataTabs[i - 1], 1))
        stop = time.time()
        howMuchData.append(len(dataTabs[i - 1]))
        timeTabs[0].append(stop - start)        

    for i in range(1, 6):
        dataTabs.append(random.sample(range(1, dataCount), dataStep * i))        
        start = time.time()                        
        sortedData.append(parallelSorting(dataTabs[i - 1], 4))
        stop = time.time()            
        timeTabs[1].append(stop - start)    

    for i in range(1, 6):
        dataTabs.append(random.sample(range(1, dataCount), dataStep * i))        
        start = time.time()                        
        sortedData.append(parallelSorting(dataTabs[i - 1], 8))
        stop = time.time()            
        timeTabs[2].append(stop - start)    

    for i in range(1, 6):
        dataTabs.append(random.sample(range(1, dataCount), dataStep * i))        
        start = time.time()                        
        sortedData.append(parallelSorting(dataTabs[i - 1], 16))
        stop = time.time()            
        timeTabs[3].append(stop - start)
    
    for i in range(1, 6):
        dataTabs.append(random.sample(range(1, dataCount), dataStep * i))        
        start = time.time()                        
        sortedData.append(parallelSorting(dataTabs[i - 1], 24))
        stop = time.time()            
        timeTabs[4].append(stop - start)
    
    plt.plot(howMuchData, timeTabs[0], 'o:r', label = '1 process')
    plt.plot(howMuchData, timeTabs[1], 'o:b', label = '4 processes')
    plt.plot(howMuchData, timeTabs[2], 'o:k', label = '8 processes')
    plt.plot(howMuchData, timeTabs[3], 'o:g', label = '16 processes')
    plt.plot(howMuchData, timeTabs[4], 'o:y', label = '24 processes')
    
    plt.legend(loc = 'upper right')
    plt.xlabel("Amount of data [num of digits]")
    plt.ylabel("Time for every amount of processes[s]")
    plt.grid()
    plt.show()