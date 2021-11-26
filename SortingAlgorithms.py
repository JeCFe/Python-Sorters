import time
def swap(i, j, Arr):
    temp = Arr[i]
    Arr[i] = Arr[j]
    Arr[j] = temp
    return Arr


def BubbleSort(Arr):
    start = time.time()
    swapped_occured = True
    while(swapped_occured):
        swapped_occured = False
        for i in range(len(Arr) - 1):
            if(Arr[i] > Arr[i + 1]):
                Arr = swap(i, i+1, Arr)
                swapped_occured = True

    return Arr

def QuickSort(Arr):  
    ArrLen = len(Arr)
    if(ArrLen < 2):
        return Arr
    pivot = 0
    for i in range(1, ArrLen):
        if(Arr[i] < Arr[0]):
            pivot += 1
            Arr = swap(i, pivot, Arr)
    Arr = swap(0, pivot, Arr)
    left = QuickSort(Arr[0:pivot])
    right = QuickSort(Arr[pivot + 1:ArrLen])
    Arr = left + [Arr[pivot]] + right
    return Arr

def SelectionSort(Arr):
    for i in range(len(Arr)):
        minIDx = i
        for j in range(i + 1, len(Arr)):
            if(Arr[minIDx] > Arr[j]):
                minIDx = j
        Arr = swap(i, minIDx, Arr)
    return Arr

def InsertionSort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i - 1
        while(j >= 0 and key < Arr[j]):
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j + 1] = key
    return Arr


def Merge(left, right):
    result = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    
    return result

def MergeSort(Arr):
    if (len(Arr) < 2):
        return Arr
    mid = int(len(Arr) / 2)
    left = MergeSort(Arr[:mid])
    right = MergeSort(Arr[mid:])
    return Merge(left, right)

    
def SorterSelector(Arr, option):
    global array
    if(option == 1):
        return BubbleSort(Arr)
    if(option == 2):
        return QuickSort(Arr)
    if(option == 3):
        return SelectionSort(Arr)
    if(option == 4):
        return InsertionSort(Arr)
    if(option == 5):
        return Arr
        #return HeapSort(Arr)
    if(option == 6):
        return MergeSort(Arr)
    
    
