import math

arr = [1,2,3,4,6,7,9,11,12,14,15,16,17,19,33,34,43,45,55,66]

def find(data):
    comparisons = 0
    lower_bound=0
    upper_bound=len(arr)

    while(lower_bound <= upper_bound):
        comparisons = comparisons + 1
        mid_point = math.ceil(lower_bound + (upper_bound - lower_bound) / 2)

        if data == arr[mid_point]:
            print("Compared count: ", comparisons)
            return mid_point
        elif arr[mid_point] < data:
            lower_bound = mid_point + 1
        else:
            upper_bound = mid_point - 1

    print(comparisons)

print("Result: ", find(50))
print("Result: ", find(3))
print("Result: ", find(43))