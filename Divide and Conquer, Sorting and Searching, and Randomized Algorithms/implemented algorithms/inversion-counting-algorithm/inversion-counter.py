def merge_and_countsplit(arr1, arr2):
    inverse_num = 0
    i = j = 0
    arr1_len, arr2_len = len(arr1), len(arr2)
    merged_arr = []
    max_len = max(arr1_len,arr2_len)
    for k in range(max_len):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
            if i == arr1_len:
                merged_arr += arr2[j:]
                break
        else:
            merged_arr.append(arr2[j])
            j += 1
            inverse_num += len(arr1[i:])
            if j == arr2_len:
                merged_arr += arr1[i:]
                break
    return (merged_arr, inverse_num)


def sort_and_count(input_arr):
    arr_len = len(input_arr)
    if arr_len <= 1:
        return (input_arr,0)
    else:
        arr1, x = sort_and_count(input_arr[:int(arr_len/2)])
        arr2, y = sort_and_count(input_arr[int(arr_len/2):])
        merged_arr, z = merge_and_countsplit(arr1,arr2)
        return (merged_arr, x + y + z)

def main():
    input = []
    with open("sample_input.txt") as numbers:
        for num in numbers:
            input.append(int(num))
    
    sorted_input,num_of_inversions = sort_and_count(input)
    print(num_of_inversions)

main()    
