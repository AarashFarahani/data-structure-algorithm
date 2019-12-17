# arr = [1,2,3,4,6,7,9,11,12,14,15,16,17,19,33,34,43,45,55,66]
arr = [1,2,3,4,6,7,9,11,12,14,15,16,17,19,33,34,43,45,55,66]

def find(data):
    comparisons = 0

    for i in range(len(arr)):
        comparisons = comparisons + 1

        if(arr[i] == data):
            print("Compared count: ", comparisons)
            return i

    print(comparisons)

print("Result: ", find(50))
print("Result: ", find(3))
print("Result: ", find(43))