def binary_search(arr, ele):
    if len(arr) == 0:
        return False
    left, right = 0, len(arr) - 1
    found = False
    while left <= right and found != True:
        mid = int((left + right) / 2)
        if arr[mid] == ele:
            found = True
        else:
            if arr[mid] < ele:
                right = mid - 1
            else:
                left = mid + 1

    return found


def rec_bin_search(arr, ele):
    # base case
    print(arr)
    if len(arr) == 0:
        return False

    # recursive case
    else:
        mid = int(len(arr) / 2)
        print(mid)
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)
            else:
                return rec_bin_search(arr[mid+1:], ele)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 5))
# print(rec_bin_search(arr, 5))
