import random


def swap(A, i, j):
    temp = A[j]
    A[j] = A[i]
    A[i] = temp

def choose_pivot(A, start, end):
    random_pivot = random.choice(A[start:end])
    pivot_index = A.index(random_pivot,start,end)
    swap(A, start, pivot_index)
    return A[start]

def quick_sort(A, start, end):
    if start >= end-1:
        return A
    
    pivot = choose_pivot(A, start, end)
    i = start
    j = start + 1
    while j < end:
        if A[j] < pivot:
            i += 1
            swap(A, i, j)
        j+=1
    swap(A, start, i)
    quick_sort(A,start,i)
    quick_sort(A,i+1,end)

def main():
    A = [1,2,4,20,2,4,7,3,8,10,15,-1,0]
    length = len(A)
    quick_sort(A, 0, length)
    print(A)

main()