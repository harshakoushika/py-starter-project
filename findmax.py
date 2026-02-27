arr = [10, 20, 30, 60, 70, 80, 90]
max = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]
print("The maximum element in the array is:", max)
