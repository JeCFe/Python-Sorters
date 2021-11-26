import random
import time

import SortingAlgorithms as SA

arrToSort = []
arrSize = 950


def PrintArr():
    global arrToSort
    print(*arrToSort, sep=",")
        
def GenerateArray():
    global arrToSort
    global arrSize
    arrToSort.clear()
    for i in range(0, arrSize):
        arrToSort.append(random.randint(0, 100))
   # PrintArr()
    
#Due to Python having a recusrive depth issue when it comes to Quick Sort this has been disabled
# def ChooseArraySize():
#      global arrSize
#      while True:
#         try:
#             inputArrSize= input("How many items do you want in the array? ")
#             arrSize = int(inputArrSize)
#             if(arrSize <= -1 or arrSize > 65535):
#                 raise ValueError
#             else:
#                 GenerateArray()
#                 break
#         except ValueError:
#             arrSize = 0
#             print("Sorry invalid entry")
#             input("Press any key to continue")
            
def Sorting(choice):
    global arrToSort
    start = time.time()
    arrToSort = SA.SorterSelector(arrToSort, choice)
    end = time.time()
    print("Time elapsed: " + str(end - start))

def CompareSorts():
    global arrToSort
    timeArr = []
    for i in range(1, 7):
        start = time.time()
        SA.SorterSelector(arrToSort, i)
        end = time.time()
        timeArr.append(end - start)
    print("Bubble Sort time: " + str(timeArr[0]))
    print("Quick Sort time: " + str(timeArr[1]))
    print("Selection Sort time: " + str(timeArr[2]))
    print("Insertion Sort time: " + str(timeArr[3]))
    print("Heap Sort time: " + str(timeArr[4]))
    print("Merge Sort time: " + str(timeArr[5]))
    
    
def MenuSelector(choice):
    if(choice >= 1 and choice <= 6):
        Sorting(choice)
        PrintArr()
        input("Press any key to continue")
        GenerateArray()
        return
    elif(choice == 7):
        GenerateArray()
    elif(choice == 8):
        PrintArr()
    elif(choice == 9):
        CompareSorts()
    
def Menu():
    while True:
        print("Choose one of the following :")
        print("[1] Bubble Sort")
        print("[2] Quick Sort")
        print ("[3] Selection Sort")
        print("[4] Insertion Sort")
        print("[5] Heap Sort")
        print("[6] Merge Sort")
        print("[7] Generate Array")
        print("[8] Show Array")
        print("[9] Compare All Sorts")
        choice = input("Menu Choice: ")
        try:
            choice = int(choice)
            if(choice >= 1 and choice <= 10):
                MenuSelector(choice)
            else:
                raise ValueError
        except ValueError:
            print("Sorry invalid entry")
            input("Press any key to continue")

def Main():
    print("-----Welcome To The SORTER-----") 
    #ChooseArraySize()
    GenerateArray()
    
    
    while True:
        menuInput = Menu()
        print(str(menuInput))


if __name__ == '__main__':
    Main()