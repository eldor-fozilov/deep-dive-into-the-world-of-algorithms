from math import inf

def abs_sum(A,k):
    sum = 0
    for i in A:
        sum += abs(i-k)
    return sum


def solution(A):
    min_num = inf
    max_num = -inf
    for i in A:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
    
    min_sum = inf
    for k in range(min_num,max_num + 1):
        temp_sum = abs_sum(A,k)
        if temp_sum < min_sum:
            min_sum = temp_sum
        else:
            break
            
    return min_sum
