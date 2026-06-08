def count_even_odd(arr):
    even = 0
    odd = 0

    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Number of Even Elements:", even)
    print("Number of Odd Elements:", odd)

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

count_even_odd(arr)
