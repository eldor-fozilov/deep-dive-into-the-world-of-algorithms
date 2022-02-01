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


def select(A, start, end, k):
    # the function will return the (k+1)th smallest numbers in the array A 
    # since array indexing will start from 0
    if start >= end-1:
        return print(A)
    
    pivot = choose_pivot(A, start, end)
    i = start
    j = start + 1
    while j < end:
        if A[j] < pivot:
            i += 1
            swap(A, i, j)
        j+=1
    swap(A, start, i)
    
    if i == k:
        print(A[i])
    elif i > k:
        select(A,start,i, k)
    else:
        select(A,i+1,end,k)

def main():
    A = [8,10,15,13,7,5,0,-6,-8,-17]
    length = len(A)
    select(A, 0, length, 4)

main()