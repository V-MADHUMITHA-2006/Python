def find_array_type(arr):
    if all(isinstance(i, int) for i in arr):
        print("Integer Array")
    elif all(isinstance(i, float) for i in arr):
        print("Float Array")
    elif all(isinstance(i, str) for i in arr):
        print("String Array")
    else:
        print("Mixed Array")


arr = [10, 20, 30, 40]

find_array_type(arr)
