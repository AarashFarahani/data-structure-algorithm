import math

# arr = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
arr = [1,2,3,4,6,7,9,11,12,14,15,16,17,19,33,34,43,45,55,66]

def find(data):
    comparisons = 0
    lo=0
    hi=len(arr)-1

    while(lo <= hi):
        comparisons = comparisons + 1

        mid = math.ceil(lo + (((hi - lo) / (arr[hi] - arr[lo])) * (data - arr[lo])))

        if mid > hi:
            break
        elif arr[mid] == data:
            print("Compared count:", comparisons)
            return mid
        elif arr[mid] < data:
            lo = mid + 1
        else:
            hi = mid - 1

print("Result: ", find(50))
print("Result: ", find(3))
print("Result: ", find(43))       