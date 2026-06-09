def find_non_repeating(arr):
    print("Non-Repeating Elements are:")

    for i in arr:
        if arr.count(i) == 1:
            print(i)

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

find_non_repeating(arr)
