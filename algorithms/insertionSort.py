'''
Docstring for algorithms.insertionSort

INSERTION-SORT pseudoCode

from j = 2  (second index) to len(arr):
    key = arr[j]
    #insert arr[j] into the sorted sequece A[1....j-1]

    i = j-1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i-1
        A[i+1] = key
    

'''
test = [5, 2, 4, 6, 1, 3]
def insertionSort(arrList):
    # Using range with indexing
    for item in range(1, len(arrList)):
        key = arrList[item]
        j = item - 1
        while j >= 0 and arrList[j] > key:
            arrList[j + 1] = arrList[j]
            j = j - 1
            arrList[j+1] = key
    print(arrList)
        


#test
insertionSort(test)