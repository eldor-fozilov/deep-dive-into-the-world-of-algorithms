def merge_sort(input_arr):
    
    n = len(input_arr)
    if n <= 1:
        return input_arr
    arr_1 = merge_sort(input_arr[:int(n/2)])
    arr_2 = merge_sort(input_arr[int(n/2):])

    i = j = 0
    merged_arr = []
    for k in range(n):
        if arr_1[i] < arr_2[j]:
            merged_arr.append(arr_1[i])
            i += 1
            if i == len(arr_1):
                merged_arr += arr_2[j:]
                break
        else:
            merged_arr.append(arr_2[j])
            j += 1
            if j == len(arr_2):
                merged_arr += arr_1[i:]
                break

    return merged_arr
