    
def abs_sum(A,k):
    sum = 0
    for num in A:
        if num - k < 0:
            sum += k - num
        else:
            sum += num - k
    return sum

def compute(A, min_num, max_num):        
    middle = (min_num + max_num) // 2
    
    mid = abs_sum(A,middle)
    low = abs_sum(A,middle - 1)
    high = abs_sum(A,middle + 1)
    if mid <= low and mid <= high:
        return mid
    elif low > mid:
        return compute(A, middle, max_num)
    elif high > mid:
        return compute(A, min_num, middle)

def solution(A):
    min_num = max_num = A[0]
    for num in A:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num
    result = compute(A, min_num, max_num)
    print(result)