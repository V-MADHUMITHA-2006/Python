def find_missing(arr):
    n = max(arr)

    for i in range(1, n + 1):
        if i not in arr:
            print("Missing element is:", i)

arr = [1, 2, 3, 5]

find_missing(arr)
