# remove duplicates and pritnunique value
arr = [10, 20, 30, 30, 40, 50, 60, 10]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)
