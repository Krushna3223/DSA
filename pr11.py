def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = [55, 44, 22, 67, 11]
print("Bubble Sort:", bubble_sort(A))


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

A = [55, 22, 11, 66, 33]
print("Insertion Sort:", insertion_sort(A))



def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

A = [55, 44, 22, 67, 11]
print("Selection Sort:", selection_sort(A))







def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

A = [12, 11, 13, 5, 6, 7]
merge_sort(A)
print("Merge Sort:", A)





def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1

def quick_sort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi-1)
        quick_sort(A, pi+1, high)

A = [10, 7, 8, 9, 1, 5]
quick_sort(A, 0, len(A)-1)
print("Quick Sort:", A)




def heapify(A, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def heap_sort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

A = [12, 11, 13, 5, 6, 7]
heap_sort(A)
print("Heap Sort:", A)
