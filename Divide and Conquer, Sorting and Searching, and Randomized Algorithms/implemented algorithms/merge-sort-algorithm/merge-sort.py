def merge_sort(input_arr):

    n = len(input_arr)
    if n <= 1:
        return input_arr
    arr_1 = merge_sort(input_arr[:int(n/2)])
    arr_2 = merge_sort(input_arr[int(n/2):])
    i = j = 0
    merged_arr = []
    len_arr1, len_arr2 = len(arr_1), len(arr_2)
    # below n (length of the input array) is used for range just for conveniece
    # since the loop will stop before k reaches n
    # the loop will execute at most ceiling of the number n/2
    for k in range(n):
        if arr_1[i] < arr_2[j]:
            merged_arr.append(arr_1[i])
            i += 1
            if i == len_arr1:
                merged_arr += arr_2[j:]
                break
        else:
            merged_arr.append(arr_2[j])
            j += 1
            if j == len_arr2:
                merged_arr += arr_1[i:]
                break

    return merged_arr


input = [1, 2, 4, 5, 10, 11, 9, 1.5]
print(merge_sort(input))
